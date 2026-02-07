"""
Analysis module – cycle times, process variants, and bottleneck detection.
"""

import pandas as pd


def cycle_times(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate cycle time (total duration) per case.

    Returns a DataFrame with columns: case_id, start, end, cycle_time.
    """
    grouped = df.groupby("case_id")["timestamp"]
    result = pd.DataFrame({
        "start": grouped.min(),
        "end": grouped.max(),
    })
    result["cycle_time"] = result["end"] - result["start"]
    return result.reset_index().sort_values("cycle_time", ascending=False)


def process_variants(df: pd.DataFrame) -> pd.DataFrame:
    """Identify unique process paths and their frequencies.

    Returns a DataFrame with columns: variant (tuple of activities), count, percentage.
    """
    variants = (
        df.sort_values(["case_id", "timestamp"])
        .groupby("case_id")["activity"]
        .apply(lambda x: " -> ".join(x))
    )
    counts = variants.value_counts().reset_index()
    counts.columns = ["variant", "count"]
    counts["percentage"] = (counts["count"] / counts["count"].sum() * 100).round(2)
    return counts


def bottlenecks(df: pd.DataFrame) -> pd.DataFrame:
    """Find activity transitions with the longest average duration.

    Returns a DataFrame with columns: from_activity, to_activity, mean_duration, occurrences.
    """
    df = df.sort_values(["case_id", "timestamp"]).copy()
    df["next_activity"] = df.groupby("case_id")["activity"].shift(-1)
    df["next_timestamp"] = df.groupby("case_id")["timestamp"].shift(-1)
    df["duration"] = df["next_timestamp"] - df["timestamp"]

    transitions = df.dropna(subset=["next_activity"]).copy()
    result = (
        transitions
        .groupby(["activity", "next_activity"])["duration"]
        .agg(["mean", "count"])
        .reset_index()
    )
    result.columns = ["from_activity", "to_activity", "mean_duration", "occurrences"]
    return result.sort_values("mean_duration", ascending=False).reset_index(drop=True)
