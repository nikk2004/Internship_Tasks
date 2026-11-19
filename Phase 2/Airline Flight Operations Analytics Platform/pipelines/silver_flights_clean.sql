-- STAGE VIEW: dedupe + cleaning (clean aur rejected dono isse padhenge)
CREATE TEMPORARY VIEW silver_flights_stage AS
WITH deduped AS (
  SELECT *
  FROM bronze_airline_flights
  -- Same flight_id ki sirf ek copy rakho
  QUALIFY ROW_NUMBER() OVER (PARTITION BY flight_id ORDER BY loaded_at) = 1
),
cleaned AS (
  SELECT
    flight_id,
    TRIM(flight_number)                                     AS flight_number,
    COALESCE(INITCAP(NULLIF(TRIM(airline), '')), 'Unknown') AS airline,
    NULLIF(TRIM(aircraft_id), '')                           AS aircraft_id,
    TRIM(aircraft_type)                                     AS aircraft_type,
    CAST(flight_date AS DATE)                               AS flight_date,
    INITCAP(TRIM(day_of_week))                              AS day_of_week,
    INITCAP(TRIM(origin_city))                              AS origin_city,
    INITCAP(TRIM(destination_city))                         AS destination_city,
    INITCAP(TRIM(origin_region))                            AS origin_region,
    distance_km,
    CAST(scheduled_departure AS TIMESTAMP)                  AS scheduled_departure,
    CAST(actual_departure    AS TIMESTAMP)                  AS actual_departure,
    -- Blank delay ho to dono times ka difference nikalo
    COALESCE(delay_minutes,
             TIMESTAMPDIFF(MINUTE,
                           CAST(scheduled_departure AS TIMESTAMP),
                           CAST(actual_departure    AS TIMESTAMP))) AS delay_minutes,
    COALESCE(INITCAP(NULLIF(TRIM(delay_reason), '')), 'Unknown')     AS delay_reason,
    seat_capacity,
    passengers,
    avg_fare,
    COALESCE(ticket_revenue, passengers * avg_fare)         AS ticket_revenue,
    fuel_cost
  FROM deduped
)
SELECT *,
  -- Negative delay (early) bhi On Time hai
  CASE WHEN delay_minutes <= 15 THEN 'On Time'
       WHEN delay_minutes <= 60 THEN 'Minor Delay'
       ELSE 'Major Delay' END AS delay_category
FROM cleaned;

-- CLEAN TABLE: sirf valid flights
CREATE OR REFRESH MATERIALIZED VIEW silver_flights_clean (
  CONSTRAINT valid_passengers EXPECT (passengers BETWEEN 0 AND seat_capacity) ON VIOLATION DROP ROW,
  CONSTRAINT valid_fare       EXPECT (avg_fare >= 0)                          ON VIOLATION DROP ROW
) AS
SELECT *
FROM silver_flights_stage
WHERE COALESCE(passengers BETWEEN 0 AND seat_capacity AND avg_fare >= 0, false);