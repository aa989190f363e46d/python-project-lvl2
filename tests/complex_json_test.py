import pytest
from gendiff.comparators.tree_gen import generate_diff_tree as generate_diff
from gendiff.formatters.plain import format_diff
from gendiff.parsers.json import parse


def test_complex_json_plain(complex_json_old, complex_json_new, complex_result_txt):
    old_map, new_map = parse(complex_json_old), parse(complex_json_new)
    test_diff = format_diff(generate_diff(old_map, new_map)).split('\n')
    ethalon_diff = complex_result_txt.read().split('\n')
    test_diff_set = set(test_diff)
    ethalon_diff_set = set(ethalon_diff)
    assert len(test_diff_set - ethalon_diff_set) == 0, 'unnecessaty diffs'
    assert len(ethalon_diff_set - test_diff_set) == 0, 'lost diffs'
