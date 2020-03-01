from gendiff.enums import ChangesEnum as changes
from gendiff.diff_tree import get_state, get_key, get_val, \
                              get_old_val, get_new_val
from typing import Mapping

CH_TAGS = {changes.ADDED: '+',
           changes.REMOVED: '-',
           changes.INTACT: ' '}
TAB = ' ' * 4
FRMT = '{}  {} {}: {}'


def format_diff(diff_tree, level=0):
    result = []
    padding = TAB * level
    for change in diff_tree:
        state = get_state(change)
        key = get_key(change)
        if state == changes.ADDED or \
           state == changes.REMOVED or \
           state == changes.INTACT:
            val = get_val(change)
            result.append(FRMT.format(
                padding, CH_TAGS[state],
                key, format_val(val, level + 1)))
        elif state == changes.ALTERED:
            old, new = get_old_val(change), get_new_val(change)
            result.append(FRMT.format(
                padding, CH_TAGS[changes.REMOVED],
                key, format_val(old, level + 1)))
            result.append(FRMT.format(
                padding, CH_TAGS[changes.ADDED],
                key, format_val(new, level + 1)))
        elif state == changes.NESTED:
            val = get_val(change)
            result.append(FRMT.format(
                padding, CH_TAGS[changes.INTACT],
                key, format_diff(val, level + 1)))
    return '{{\n{}\n{}}}'.format('\n'.join(result), padding)


def format_val(val, level):
    result = []
    padding = TAB * level
    if isinstance(val, Mapping):
        for k, v in val.items():
            result.append('{}{}: {}'.format(padding + TAB,
                                            k,
                                            format_val(v, level + 1)))
            return '{{\n{}\n{}}}'.format('\n'.join(result),
                                         padding)
    else:
        return '{}'.format(val)
