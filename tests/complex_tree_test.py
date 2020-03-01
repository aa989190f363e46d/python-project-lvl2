import pytest
from operator import contains

from gendiff.enums import ChangesEnum as changes
from gendiff.diff_tree import get_state, get_key, get_val, \
                              get_old_val, get_new_val  
from gendiff.comparators.tree_gen import generate_diff_tree as generate_diff
from gendiff.parsers.json import parse


def test_complex_tree(complex_json_old, complex_json_new, complex_diff):
    old_map, new_map = parse(complex_json_old), parse(complex_json_new)
    test_diff = generate_diff(old_map, new_map)
    assert check_diff_nesting(test_diff, complex_diff)
    assert check_diff_nesting(complex_diff, test_diff)


def check_diff_nesting(diff, subdiff):
    for change in subdiff:
        state = get_state(change)
        if state == changes.NESTED:
            res = check_diff_nesting(diff, get_val(change))
        else:
            res = find_in_diff(diff, change)
        if not res:
            return False
    return True


def find_in_diff(diff, target_change):
    target_state = get_state(target_change)
    target_key = get_key(target_change)
    res = False
    for i, change in enumerate(diff):
        state = get_state(change)
        if state == changes.NESTED:
            res = find_in_diff(get_val(change), target_change)
        else:
            if get_key(change) == target_key and \
               state == target_state:
                if state == changes.ALTERED:
                    res = get_old_val(change) == get_old_val(target_change) and \
                          get_new_val(change) == get_new_val(target_change)
                else:
                    res = get_val(change) == get_val(target_change)
            else:
                res = False
        if res:
            return True
    return False
