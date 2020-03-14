from typing import Mapping

from gendiff.diff_tree import ADDED, REMOVED, ALTERED, NESTED

TAGS = {ADDED: 'added',
        REMOVED: 'removed',
        ALTERED: 'changed'}

MESSAGE_FORMAT = "Property '{}' was {}{}"


def format_diff(diff_tree, parent=''):
    result = []
    for state, key, value in diff_tree:
        full_key = '{}.{}'.format(parent, key) if parent else key
        if state in (ADDED, REMOVED, ALTERED):
            result.append(MESSAGE_FORMAT.format(full_key,
                          TAGS[state],
                          format_value(value, state)))
        elif state == NESTED:
            result.append(format_diff(value, full_key))
    return '\n'.join(result)


def format_value(value, change):
    if isinstance(value, Mapping):
        return " with value: 'complex value'"
    else:
        if change == ALTERED:
            return ". From '{}' to '{}'".format(*value)
        else:
            return " with value: {}".format(value)
