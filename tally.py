RATE_PENCE = 5


def parse_line(line):
    fields = line.split(",")
    if len(fields) != 2:
        raise ValueError("a line must have exactly two comma-separated fields")
    item = fields[0].strip()
    count_text = fields[1].strip()
    if not item:
        raise ValueError("the item field must not be empty")
    if not count_text.isdigit():
        raise ValueError("the count field must be a non-negative integer")
    return item, int(count_text)


def line_pence(count, unit_pence=RATE_PENCE):
    return count * unit_pence


def total_pence(lines):
    return sum(line_pence(count) for _, count in lines)


def format_pence(pence):
    pounds, pence_part = divmod(pence, 100)
    return f"{pounds}.{pence_part:02d}"
