from typing import Mapping

ADDED = 'ADDED'
REMOVED = 'REMOVED'
ALTERED = 'ALTERED'
NESTED = 'NESTED'

CH_TAGS = {ADDED: 'added',
           REMOVED: 'removed',
           ALTERED: 'changed'}

FRMT = "Property '{}' was {}{}"


def format_diff(diff_tree, parent=''):
    result = []
    for state, key, value in diff_tree:
        full_key = '{}.{}'.format(parent, key) if parent else key
        if state in (ADDED, REMOVED, ALTERED):
            result.append(FRMT.format(full_key,
                          CH_TAGS[state],
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
