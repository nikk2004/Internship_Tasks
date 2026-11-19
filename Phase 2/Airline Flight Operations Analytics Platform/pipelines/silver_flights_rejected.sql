-- REJECTED TABLE: bad flights + reason
-- Stage view se padh rahe hain (dedupe + cleaning ho chuki hai)
CREATE OR REFRESH MATERIALIZED VIEW silver_flights_rejected AS
SELECT *,
  CASE WHEN passengers > seat_capacity THEN 'Passengers more than seats'
       WHEN passengers < 0             THEN 'Passengers is negative'
       WHEN avg_fare < 0               THEN 'Average fare is negative'
       ELSE 'Missing passengers/fare/seats' END AS reject_reason
FROM silver_flights_stage
-- Clean table ka exact ulta condition
WHERE NOT COALESCE(passengers BETWEEN 0 AND seat_capacity AND avg_fare >= 0, false);