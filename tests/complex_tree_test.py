import pytest

from gendiff.parsers import parse_json
from gendiff.diff_tree import generate_diff


@pytest.fixture()
def complex_diff():
    return [['NESTED','common',
                [['INTACT','setting1','Value 1'],
                 ['INTACT','setting3',True],
                 ['ADDED','setting4','blah blah'],
                 ['ADDED','setting5',{'key5':'value5'}],
                 ['REMOVED','setting2','200'],
                 ['REMOVED','setting6',{'key':'value'}]]],
            ['NESTED','group1',
                [['ALTERED','baz',
                 ['bas','bars']],
                 ['INTACT','foo','bar']]],
            ['ADDED','group3',{'fee':'100500'}],
            ['REMOVED','group2',{'abc':'12345'}]]


def test_complex_tree(complex_json_old, complex_json_new, complex_diff):
    old_map, new_map = parse_json(complex_json_old), parse_json(complex_json_new)
    test_diff = generate_diff(old_map, new_map)
    assert test_diff == complex_diff
    