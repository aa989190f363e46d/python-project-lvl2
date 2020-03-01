import pytest
from gendiff.comparators.tree_gen import generate_diff_tree as generate_diff
from gendiff.formatters.plain import format_diff
from gendiff.parsers.yaml import parse


def test_complex_yaml(complex_yaml_old, complex_yaml_new, complex_result_txt):
    old_map, new_map = parse(complex_yaml_old), parse(complex_yaml_new)
    test_diff = format_diff(generate_diff(old_map, new_map)).split('\n')
    ethalon_diff = complex_result_txt.read().split('\n')
    assert test_diff[0] == ethalon_diff[0], 'first line not equal'
    assert test_diff[-1] == ethalon_diff[-1], 'last line not equal'
    test_diff_set = set(test_diff[1:-1])
    ethalon_diff_set = set(ethalon_diff[1:-1])
    assert len(test_diff_set - ethalon_diff_set) == 0, 'unnecessaty diffs'
    assert len(ethalon_diff_set - test_diff_set) == 0, 'lost diffs'
