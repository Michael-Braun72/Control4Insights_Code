"""
Data loading module – reads CSV and Excel files into a standardized DataFrame.
"""

import pathlib

import pandas as pd

from config import COLUMN_MAPPING, TIMESTAMP_FORMAT


def load_event_log(filepath: str) -> pd.DataFrame:
    """Load an event log from a CSV or Excel file.

    Returns a DataFrame with normalized columns: case_id, activity, timestamp.
    """
    path = pathlib.Path(filepath)
    ext = path.suffix.lower()

    if ext == ".csv":
        df = pd.read_csv(filepath)
    elif ext in (".xls", ".xlsx"):
        df = pd.read_excel(filepath, engine="openpyxl" if ext == ".xlsx" else "xlrd")
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    _validate_columns(df)
    df = _normalize(df)
    return df


def _validate_columns(df: pd.DataFrame) -> None:
    """Ensure all required columns are present."""
    missing = [
        col for col in COLUMN_MAPPING.values() if col not in df.columns
    ]
    if missing:
        raise KeyError(
            f"Missing required columns: {missing}. "
            f"Available columns: {list(df.columns)}. "
            f"Adjust COLUMN_MAPPING in config.py if needed."
        )


def _normalize(df: pd.DataFrame) -> pd.DataFrame:
    """Rename columns to internal names and parse timestamps."""
    reverse_map = {v: k for k, v in COLUMN_MAPPING.items()}
    df = df.rename(columns=reverse_map)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format=TIMESTAMP_FORMAT)
    df = df.sort_values(["case_id", "timestamp"]).reset_index(drop=True)
    return df
