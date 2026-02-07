"""
Process Analyzer – Entry point.

Usage:
    python main.py <path-to-event-log>
    python main.py data/sample_event_log.csv
"""

import sys

from loader import load_event_log
from analysis import cycle_times, process_variants, bottlenecks
from visualization import (
    plot_cycle_times,
    plot_variants,
    plot_bottlenecks,
    plot_process_flow,
)


def run(filepath: str) -> None:
    print(f"Loading event log: {filepath}")
    df = load_event_log(filepath)
    print(f"  {len(df)} events loaded across {df['case_id'].nunique()} cases.\n")

    # --- Cycle Times ---
    ct = cycle_times(df)
    print("Cycle Times (top 10):")
    print(ct.head(10).to_string(index=False))
    path = plot_cycle_times(ct)
    print(f"  -> Chart saved: {path}\n")

    # --- Process Variants ---
    pv = process_variants(df)
    print("Process Variants (top 10):")
    print(pv.head(10).to_string(index=False))
    path = plot_variants(pv)
    print(f"  -> Chart saved: {path}\n")

    # --- Bottlenecks ---
    bn = bottlenecks(df)
    print("Bottlenecks (top 10):")
    print(bn.head(10).to_string(index=False))
    path = plot_bottlenecks(bn)
    print(f"  -> Chart saved: {path}\n")

    # --- Process Flow ---
    path = plot_process_flow(pv)
    print(f"Process flow chart saved: {path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path-to-event-log>")
        print("Supported formats: .csv, .xls, .xlsx")
        sys.exit(1)
    run(sys.argv[1])
