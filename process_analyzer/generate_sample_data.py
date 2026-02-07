"""Generate a sample event log CSV for testing the process analyzer."""

import csv
import random
from datetime import datetime, timedelta

ACTIVITIES_SETS = [
    ["Order Received", "Payment Verified", "Item Picked", "Item Packed", "Shipped", "Delivered"],
    ["Order Received", "Payment Verified", "Item Picked", "Item Packed", "Shipped", "Return Requested"],
    ["Order Received", "Payment Verified", "Item Out of Stock", "Customer Notified", "Order Cancelled"],
    ["Order Received", "Payment Verified", "Item Picked", "Quality Check", "Item Packed", "Shipped", "Delivered"],
]

WEIGHTS = [50, 15, 10, 25]


def generate(num_cases: int = 200, output: str = "data/sample_event_log.csv") -> None:
    rows = []
    for case_id in range(1, num_cases + 1):
        activities = random.choices(ACTIVITIES_SETS, weights=WEIGHTS, k=1)[0]
        ts = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 90))
        for activity in activities:
            rows.append([f"C-{case_id:04d}", activity, ts.strftime("%Y-%m-%d %H:%M:%S")])
            ts += timedelta(hours=random.randint(1, 48), minutes=random.randint(0, 59))

    with open(output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Case ID", "Activity", "Timestamp"])
        writer.writerows(rows)

    print(f"Generated {len(rows)} events for {num_cases} cases -> {output}")


if __name__ == "__main__":
    generate()
