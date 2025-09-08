"""Sales analysis helpers."""

import csv


def load_sales(path):
    """Read a sales CSV file and return a list of dictionaries (one per row)."""
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def total_revenue(rows):
    """Sum quantity * unit_price over all rows."""
    if not rows:
        return 0.0
    return sum(float(r["quantity"]) * float(r["unit_price"]) for r in rows)
