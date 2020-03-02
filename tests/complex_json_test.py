import pytest
from gendiff.comparators.tree_gen import generate_diff_tree as generate_diff
from gendiff.formatters.selector import select as select_formatter
from gendiff.parsers.json import parse
from json import load, loads

def test_complex_json_plain(complex_json_old, complex_json_new, complex_result_txt):
    format_diff = select_formatter('plain')
    old_map, new_map = parse(complex_json_old), parse(complex_json_new)
    test_diff = format_diff(generate_diff(old_map, new_map)).split('\n')
    ethalon_diff = complex_result_txt.read().split('\n')
    test_diff_set = set(test_diff)
    ethalon_diff_set = set(ethalon_diff)
    assert len(test_diff_set - ethalon_diff_set) == 0, 'unnecessary diffs'
    assert len(ethalon_diff_set - test_diff_set) == 0, 'lost diffs'


def test_complex_json_json(complex_json_old, complex_json_new, complex_result_json):
    format_diff = select_formatter('json')
    old_map, new_map = parse(complex_json_old), parse(complex_json_new)
    test_diff = loads(format_diff(generate_diff(old_map, new_map)))
    ethalon_diff = load(complex_result_json)
    assert test_diff == ethalon_diff
