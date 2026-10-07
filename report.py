from tabulate import tabulate


def render_table(lines):
    rows = [(item, count) for item, count in lines]
    return tabulate(rows, headers=["item", "count"])
