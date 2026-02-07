"""
Configuration for process analyzer.
Adjust COLUMN_MAPPING if your source data uses different column names.
"""

# Map internal names to actual column names in your data file.
COLUMN_MAPPING = {
    "case_id": "Case ID",
    "activity": "Activity",
    "timestamp": "Timestamp",
}

# Timestamp format used in the source data (None = auto-detect).
TIMESTAMP_FORMAT = None

# Maximum number of process variants to display in charts.
TOP_VARIANTS = 10
