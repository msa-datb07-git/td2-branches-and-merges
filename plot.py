"""Bar chart of revenue by region (text version, no external dependency)."""

from analysis import load_sales, revenue_by_region


def text_bar_chart(values, width=40):
    biggest = max(values.values())
    for label, value in values.items():
        bar = "#" * int(width * value / biggest)
        print(f"{label:<8} {bar} {value:.2f}")


if __name__ == "__main__":
    text_bar_chart(revenue_by_region(load_sales("data/sales.csv")))
