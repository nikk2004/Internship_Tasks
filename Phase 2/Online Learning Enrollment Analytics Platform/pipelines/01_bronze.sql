-- =====================================================
-- BRONZE LAYER: raw course enrollments
-- Keeps the source data exactly as it is (no cleaning)
-- =====================================================

-- STREAMING TABLE = reads only new files each time the pipeline runs
CREATE OR REFRESH STREAMING TABLE bronze_course_enrollments AS
SELECT
  *,                                   -- all 20 source columns
  _metadata.file_name AS source_file,  -- which file the row came from
  current_timestamp() AS loaded_at     -- when the row was loaded
FROM STREAM read_files(
  '/Volumes/edtech_catalog/learning/raw_files/',  -- Unity Catalog Volume path
  format => 'csv',                                -- file type
  header => true                                  -- first row = column names
);