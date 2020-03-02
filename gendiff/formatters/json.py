from gendiff.diff_structure.enums import ChangesEnum as changes
from gendiff.diff_structure.tree import get_state, get_key, get_val, \
                                        get_old_val, get_new_val

from json import dumps

CH_TAGS = {changes.ADDED: 'add',
           changes.REMOVED: 'delete',
           changes.ALTERED: 'alternate',
           changes.INTACT: 'preserve'}


def format_diff(diff_tree):
    return dumps({'diff': build_tree(diff_tree)})


def build_tree(diff_tree):
    result = {}
    for change in diff_tree:
        state = get_state(change)
        key = get_key(change)
        val = get_val(change)
        if state in (changes.REMOVED,
                     changes.ADDED,
                     changes.INTACT):
            result[key] = {'event': CH_TAGS[state],
                           'value': val}
        elif state == changes.ALTERED:
            result[key] = {'event': CH_TAGS[state],
                           'old_value': get_old_val(change),
                           'new_value': get_new_val(change)}
        elif state == changes.NESTED:
            result[key] = build_tree(val)
    return result
