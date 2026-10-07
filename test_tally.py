import pytest

import tally


def test_parse_line_splits_item_and_count():
    assert tally.parse_line("apples, 3") == ("apples", 3)


def test_parse_line_rejects_wrong_field_count():
    with pytest.raises(ValueError):
        tally.parse_line("apples,3,extra")


def test_line_pence_multiplies():
    assert tally.line_pence(4, unit_pence=25) == 100


def test_total_pence_sums_lines():
    lines = [("apples", 2), ("pears", 3)]
    assert tally.total_pence(lines) == tally.line_pence(2) + tally.line_pence(3)


def test_format_pence_pads_pence():
    assert tally.format_pence(1005) == "10.50"
