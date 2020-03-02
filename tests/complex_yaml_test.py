import pytest
from gendiff.comparators.tree_gen import generate_diff_tree as generate_diff
from gendiff.formatters.selector import select as select_formatter
from gendiff.parsers.yaml import parse
from yaml import load, Loader


def test_complex_yaml_plain(complex_yaml_old, complex_yaml_new, complex_result_txt):
    format_diff = select_formatter('plain')
    old_map, new_map = parse(complex_yaml_old), parse(complex_yaml_new)
    test_diff = format_diff(generate_diff(old_map, new_map)).split('\n')
    ethalon_diff = complex_result_txt.read().split('\n')
    test_diff_set = set(test_diff)
    ethalon_diff_set = set(ethalon_diff)
    assert len(test_diff_set - ethalon_diff_set) == 0, 'unnecessary diffs'
    assert len(ethalon_diff_set - test_diff_set) == 0, 'lost diffs'


def test_complex_yaml_yaml(complex_yaml_old, complex_yaml_new, complex_result_yaml):
    format_diff = select_formatter('yaml')
    old_map, new_map = parse(complex_yaml_old), parse(complex_yaml_new)
    test_diff = load(format_diff(generate_diff(old_map, new_map)), Loader=Loader)
    ethalon_diff = load(complex_result_yaml, Loader=Loader)
    assert test_diff == ethalon_diff
