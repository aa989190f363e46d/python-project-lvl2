from gendiff.enums import ChangesEnum as changes


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
