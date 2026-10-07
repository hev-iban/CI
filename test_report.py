import report


def test_render_table_contains_header_and_item():
    output = report.render_table([("apples", 3), ("pears", 1)])
    assert "item" in output
    assert "count" in output
    assert "apples" in output
