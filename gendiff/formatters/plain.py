from gendiff.enums import ChangesEnum as changes
from gendiff.diff_tree import get_state, get_key, get_val
from typing import Mapping

CH_TAGS = {changes.ADDED: 'added',
           changes.REMOVED: 'removed',
           changes.ALTERED: 'changed'}
FRMT = "Property '{}' was {}{}"


def format_diff(diff_tree, parent=''):
    result = []
    for change in diff_tree:
        state = get_state(change)
        key = get_key(change)
        val = get_val(change)
        _key = '{}.{}'.format(parent, key) if parent else key
        if state in (changes.ADDED,
                     changes.REMOVED,
                     changes.ALTERED):
            result.append(FRMT.format(_key,
                          CH_TAGS[state],
                          format_val(val, state)))
        elif state == changes.NESTED:
            result.append(format_diff(val, _key))
    return '\n'.join(result)


def format_val(val, change):
    if isinstance(val, Mapping):
        return " with value: 'complex value'"
    else:
        if change == changes.ALTERED:
            return ". From '{}' to '{}'".format(*val)
        else:
            return " with value: {}".format(val)
