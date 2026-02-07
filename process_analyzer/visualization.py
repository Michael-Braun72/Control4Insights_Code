"""
Visualization module – charts and flow diagrams for process analysis results.
"""

import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from config import TOP_VARIANTS

OUTPUT_DIR = pathlib.Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def plot_cycle_times(ct: pd.DataFrame, output: str | None = None) -> str:
    """Horizontal bar chart of cycle times per case."""
    top = ct.head(30).copy()
    top["hours"] = top["cycle_time"].dt.total_seconds() / 3600

    fig, ax = plt.subplots(figsize=(10, max(4, len(top) * 0.35)))
    ax.barh(top["case_id"].astype(str), top["hours"], color="#4c72b0")
    ax.set_xlabel("Cycle Time (hours)")
    ax.set_title("Cycle Time per Case (Top 30)")
    ax.invert_yaxis()
    plt.tight_layout()

    path = output or str(OUTPUT_DIR / "cycle_times.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def plot_variants(variants: pd.DataFrame, output: str | None = None) -> str:
    """Bar chart of the most frequent process variants."""
    top = variants.head(TOP_VARIANTS).copy()
    labels = [v if len(v) < 60 else v[:57] + "..." for v in top["variant"]]

    fig, ax = plt.subplots(figsize=(10, max(4, len(top) * 0.5)))
    ax.barh(labels, top["count"], color="#55a868")
    ax.set_xlabel("Count")
    ax.set_title(f"Top {len(top)} Process Variants")
    ax.invert_yaxis()
    plt.tight_layout()

    path = output or str(OUTPUT_DIR / "variants.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def plot_bottlenecks(bn: pd.DataFrame, output: str | None = None) -> str:
    """Bar chart of transitions with the longest average duration."""
    top = bn.head(15).copy()
    top["hours"] = top["mean_duration"].dt.total_seconds() / 3600
    labels = top["from_activity"] + " -> " + top["to_activity"]

    fig, ax = plt.subplots(figsize=(10, max(4, len(top) * 0.4)))
    ax.barh(labels, top["hours"], color="#c44e52")
    ax.set_xlabel("Mean Duration (hours)")
    ax.set_title("Bottlenecks – Slowest Transitions (Top 15)")
    ax.invert_yaxis()
    plt.tight_layout()

    path = output or str(OUTPUT_DIR / "bottlenecks.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def plot_process_flow(variants: pd.DataFrame, output: str | None = None) -> str:
    """Simple text-based flow chart of the most common process variant.

    Uses graphviz if available, otherwise falls back to a matplotlib text diagram.
    """
    top_variant = variants.iloc[0]["variant"]
    steps = [s.strip() for s in top_variant.split("->")]

    try:
        import graphviz
        dot = graphviz.Digraph(format="png")
        dot.attr(rankdir="LR", size="12,4")
        dot.attr("node", shape="box", style="rounded,filled", fillcolor="#d9e6f2")

        for i, step in enumerate(steps):
            dot.node(str(i), step)
        for i in range(len(steps) - 1):
            dot.edge(str(i), str(i + 1))

        path = output or str(OUTPUT_DIR / "process_flow")
        dot.render(path, cleanup=True)
        return path + ".png"

    except Exception:
        # Fallback: matplotlib text flow
        fig, ax = plt.subplots(figsize=(max(8, len(steps) * 2), 2))
        ax.set_xlim(0, len(steps))
        ax.set_ylim(0, 1)
        ax.axis("off")
        ax.set_title("Most Common Process Path", fontsize=13)

        for i, step in enumerate(steps):
            ax.text(
                i + 0.5, 0.5, step,
                ha="center", va="center", fontsize=9,
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#d9e6f2", edgecolor="#333"),
            )
            if i < len(steps) - 1:
                ax.annotate(
                    "", xy=(i + 1.05, 0.5), xytext=(i + 0.95, 0.5),
                    arrowprops=dict(arrowstyle="->", lw=1.5),
                )

        plt.tight_layout()
        path = output or str(OUTPUT_DIR / "process_flow.png")
        fig.savefig(path, dpi=150)
        plt.close(fig)
        return path
