from typing import Mapping

from gendiff.diff_tree import ADDED, REMOVED, ALTERED, NESTED, INTACT

TAGS = {ADDED: '+',
        REMOVED: '-',
        INTACT: ' '}

TAB = ' ' * 2


def format_diff(tree, root_key=None, level=1):
    result = []
    for state, key, value in tree:
        if state in (ADDED, REMOVED, INTACT):
            result.append(
              format_value(key, value, TAGS[state], level))
        elif state == ALTERED:
            result.append(
              format_value(key, value[0], TAGS[REMOVED], level))
            result.append(
              format_value(key, value[1], TAGS[ADDED], level))
        elif state == NESTED:
            result.append(format_diff(value, key, level + 1))
    return wrap_with_braces('\n'.join(result), level, root_key)


def format_value(key, value, change='', level=0):
    if isinstance(value, Mapping):
        return format_tree_value(key, value, change, level)
    else:
        return format_simple_value(key, value, change, level)


def format_simple_value(key, value, change=' ', level=0):
    return '{}{}{} {}: {}'.format(
      TAB * level,
      TAB[:-2],
      change,
      key, value)


def format_tree_value(key, value, change=' ', level=0):
    result = [format_simple_value(key, '{', change, level)]
    for nested_key, nested_value in value.items():
        if isinstance(nested_value, Mapping):
            result.append(format_tree_value(
              nested_key, nested_value, ' ', level + 1))
        else:
            result.append(format_simple_value(
              nested_key, nested_value, ' ', level + 1))
    return '{}\n{}}}'.format(
      '\n'.join(result),
      TAB * level)


def wrap_with_braces(string, level, key=None):
    return '{}{}{{\n{}\n{}}}'.format(
      TAB * (level - 1),
      '{}: '.format(key) if key else '',
      string,
      TAB * (level - 1))
