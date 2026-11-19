-- =====================================================
-- SILVER LAYER: cleaned and rejected enrollments
-- =====================================================

-- ---------- Clean table ----------
-- EXPECT = data quality rule
-- ON VIOLATION DROP ROW = remove rows that break the rule (and count them)
CREATE OR REFRESH MATERIALIZED VIEW silver_enrollments_clean (
  CONSTRAINT valid_progress EXPECT (progress_pct BETWEEN 0 AND 100) ON VIOLATION DROP ROW,
  CONSTRAINT valid_price    EXPECT (price_paid >= 0)                ON VIOLATION DROP ROW
) AS
WITH cleaned AS (
  -- SELECT DISTINCT removes fully duplicated rows
  SELECT DISTINCT
    enrollment_id,
    learner_id,                                   -- keep blanks as they are
    LOWER(TRIM(learner_email)) AS learner_email,  -- emails must be lower case (never INITCAP)
    COALESCE(NULLIF(INITCAP(TRIM(learner_city)), ''), 'Unknown') AS learner_city,  -- blank city -> Unknown
    age_group,
    course_id,
    TRIM(course_name) AS course_name,             -- remove extra spaces
    COALESCE(NULLIF(INITCAP(TRIM(category)), ''), 'Unknown') AS category,          -- blank category -> Unknown
    INITCAP(TRIM(course_level))       AS course_level,        -- Title Case, no extra spaces
    TRIM(instructor_name)             AS instructor_name,
    enrollment_date,
    INITCAP(TRIM(enrollment_channel)) AS enrollment_channel,  -- Title Case, no extra spaces
    list_price,
    discount_amount,
    -- if price_paid is blank, calculate it as list_price - discount_amount
    COALESCE(price_paid, list_price - discount_amount) AS price_paid,
    payment_method,
    progress_pct,
    hours_watched,
    course_rating,                                -- keep blank ratings as NULL (AVG skips NULLs)
    certificate_issued
  FROM bronze_course_enrollments
)
SELECT
  *,
  -- new column: learner status based on progress
  CASE WHEN progress_pct = 100 THEN 'Completed'
       WHEN progress_pct > 0   THEN 'In Progress'
       ELSE 'Not Started' END AS learner_status
FROM cleaned;


-- ---------- Rejected table ----------
-- Rows removed from the clean table, saved with a reason
CREATE OR REFRESH MATERIALIZED VIEW silver_enrollments_rejected AS
SELECT DISTINCT                                    -- avoid counting duplicate rows again
  * EXCEPT (source_file, loaded_at),               -- these two columns change on every run
  CASE WHEN progress_pct < 0 OR progress_pct > 100
         THEN 'Progress is outside 0 to 100'
       ELSE 'Price paid is negative'
  END AS reject_reason                             -- why the row was rejected
FROM bronze_course_enrollments
WHERE progress_pct < 0       -- progress below 0
   OR progress_pct > 100     -- progress above 100
   OR price_paid < 0;        -- negative price