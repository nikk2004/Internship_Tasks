-- =====================================================
-- GOLD LAYER: business-ready summary tables
-- All Gold tables read from the clean Silver table only
-- =====================================================

-- ---------- GOLD 1: monthly enrollments (BR-01) ----------
CREATE OR REFRESH MATERIALIZED VIEW gold_monthly_enrollments AS
SELECT
  DATE_TRUNC('MONTH', enrollment_date) AS enrollment_month,   -- first day of the month
  COUNT(*)                             AS enrollments,        -- all enrollments in the month
  COUNT(DISTINCT learner_email)        AS unique_learners,    -- same learner counted once
  SUM(price_paid)                      AS revenue,            -- money actually paid
  SUM(discount_amount)                 AS total_discount,
  SUM(CASE WHEN learner_status = 'Completed' THEN 1 ELSE 0 END) AS completions,
  SUM(hours_watched)                   AS hours_watched
FROM silver_enrollments_clean
GROUP BY DATE_TRUNC('MONTH', enrollment_date);


-- ---------- GOLD 2: category summary (BR-02) ----------
CREATE OR REFRESH MATERIALIZED VIEW gold_category_summary AS
SELECT
  category,
  COUNT(*)         AS enrollments,
  SUM(price_paid)  AS revenue,
  SUM(CASE WHEN learner_status = 'Completed'   THEN 1 ELSE 0 END) AS completed,
  SUM(CASE WHEN learner_status = 'In Progress' THEN 1 ELSE 0 END) AS in_progress,
  SUM(CASE WHEN learner_status = 'Not Started' THEN 1 ELSE 0 END) AS not_started,
  -- completion rate = completed * 100 / all enrollments (100.0 forces decimal division)
  ROUND(SUM(CASE WHEN learner_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS completion_rate_pct,
  ROUND(AVG(progress_pct), 2) AS avg_progress_pct
FROM silver_enrollments_clean
GROUP BY category;


-- ---------- GOLD 3: course summary (BR-03) ----------
CREATE OR REFRESH MATERIALIZED VIEW gold_course_summary AS
SELECT
  category,
  course_name,
  course_level,
  instructor_name,
  COUNT(*)        AS enrollments,
  SUM(price_paid) AS revenue,
  ROUND(SUM(CASE WHEN learner_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS completion_rate_pct,
  ROUND(AVG(course_rating), 2) AS avg_rating,      -- AVG skips NULL ratings automatically
  ROUND(SUM(hours_watched), 1) AS hours_watched
FROM silver_enrollments_clean
GROUP BY category, course_name, course_level, instructor_name;


-- ---------- GOLD 4: channel summary (BR-04) ----------
CREATE OR REFRESH MATERIALIZED VIEW gold_channel_summary AS
SELECT
  enrollment_channel,
  COUNT(*)        AS enrollments,
  SUM(price_paid) AS revenue,
  ROUND(SUM(CASE WHEN learner_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS completion_rate_pct
FROM silver_enrollments_clean
GROUP BY enrollment_channel;


-- ---------- GOLD 5: data quality + reconciliation (BR-05, BR-06) ----------
CREATE OR REFRESH MATERIALIZED VIEW gold_data_quality AS
SELECT
  COUNT(*)                                        AS bronze_rows,
  COUNT(*) - COUNT(DISTINCT enrollment_id)        AS duplicate_rows,
  -- distinct enrollment_id so duplicated bad rows are not counted twice
  COUNT(DISTINCT CASE WHEN progress_pct < 0 OR progress_pct > 100
                      THEN enrollment_id END)     AS invalid_progress_rows,
  COUNT(DISTINCT CASE WHEN price_paid < 0
                      THEN enrollment_id END)     AS negative_price_rows,
  COUNT(DISTINCT CASE WHEN category IS NULL OR TRIM(category) = ''
                      THEN enrollment_id END)     AS missing_category_rows,
  COUNT(DISTINCT CASE WHEN learner_city IS NULL OR TRIM(learner_city) = ''
                      THEN enrollment_id END)     AS missing_city_rows,
  COUNT(DISTINCT CASE WHEN price_paid IS NULL
                      THEN enrollment_id END)     AS missing_price_rows,
  -- learners before the email fix (messy emails look like different people)
  COUNT(DISTINCT learner_email)                   AS learners_before_email_fix,
  -- learners after the email fix (trimmed + lower case)
  COUNT(DISTINCT LOWER(TRIM(learner_email)))      AS learners_after_email_fix,
  -- how many learners were double-counted because of messy emails
  COUNT(DISTINCT learner_email) - COUNT(DISTINCT LOWER(TRIM(learner_email))) AS double_counted_learners,
  (SELECT COUNT(*) FROM silver_enrollments_clean)    AS clean_rows,
  (SELECT COUNT(*) FROM silver_enrollments_rejected) AS rejected_rows
FROM bronze_course_enrollments;