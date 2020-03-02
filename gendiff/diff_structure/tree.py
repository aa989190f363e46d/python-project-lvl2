from gendiff.diff_structure.enums import ChangesEnum as changes


def make_tree():
    return []


def add_altered(tree, key, old_val, new_val):
    generic_add(tree, changes.ALTERED, key, (old_val, new_val))


def add_removed(tree, key, val):
    generic_add(tree, changes.REMOVED, key, val)


def add_added(tree, key, val):
    generic_add(tree, changes.ADDED, key, val)


def add_intact(tree, key, val):
    generic_add(tree, changes.INTACT, key, val)


def add_nested(tree, key, sub):
    generic_add(tree, changes.NESTED, key, sub)


def generic_add(tree, change, key, val):
    tree.append([change, key, val])


def get_state(tree):
    return tree[0]


def get_key(tree):
    return tree[1]


def get_val(change):
    return change[2]


def get_old_val(change):
    if get_state(change) == changes.ALTERED:
        return get_val(change)[0]


def get_new_val(change):
    if get_state(change) == changes.ALTERED:
        return get_val(change)[1]


CH_TAGS = {changes.ADDED: 'add',
           changes.REMOVED: 'delete',
           changes.ALTERED: 'alternate',
           changes.INTACT: 'preserve'}


def dump_tree(diff_tree):
    result = {}
    for change in diff_tree:
        state = get_state(change)
        key, val = get_key(change), get_val(change)
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
            result[key] = dump_tree(val)
    return result
