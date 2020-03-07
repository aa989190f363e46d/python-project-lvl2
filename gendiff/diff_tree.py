from typing import Mapping

ADDED = 'ADDED'
REMOVED = 'REMOVED'
ALTERED = 'ALTERED'
NESTED = 'NESTED'
INTACT = 'INTACT'


def generate_diff(old_tree_map, new_tree_map):
    old_keys, new_keys = old_tree_map.keys(), new_tree_map.keys()
    diff = []
    for k in sorted(list(old_keys & new_keys)):
        old_val, new_val = old_tree_map[k], new_tree_map[k]
        if not (isinstance(old_val, Mapping) and isinstance(new_val, Mapping)):
            if old_val == new_val:
                diff.append([INTACT, k, old_val])
            else:
                diff.append([ALTERED, k, [old_val, new_val]])
        else:
            diff.append([NESTED, k, generate_diff(old_val, new_val)])
    for k in sorted(list(new_keys - old_keys)):
        diff.append([ADDED, k, new_tree_map[k]])
    for k in sorted(list(old_keys - new_keys)):
        diff.append([REMOVED, k, old_tree_map[k]])
    return diff
