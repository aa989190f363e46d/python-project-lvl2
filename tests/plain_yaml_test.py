import pytest
from gendiff.comparators.plain_map import generate_diff
from gendiff.parsers.yaml import parse


def test_plain_json():
    with open('tests/fixtures/plain_yaml_before.yml') as old, \
        open('tests/fixtures/plain_yaml_after.yml') as new, \
        open('tests/fixtures/plain_yaml_result.txt') as result:
        old_map, new_map = parse(old), parse(new)
        test_diff = generate_diff(old_map, new_map).split('\n')
        ethalon_diff = result.read().split('\n')[:-1]
        assert test_diff[0] == ethalon_diff[0], 'first lines not equal'
        assert test_diff[-1] == ethalon_diff[-1], 'last lines not equal'
        test_diff_set = set(test_diff[1:-1])
        ethalon_diff_set = set(ethalon_diff[1:-1])
        assert len(test_diff_set - ethalon_diff_set) == 0, 'unnecessaty diffs'
        assert len(ethalon_diff_set - test_diff_set) == 0, 'lost diffs'
