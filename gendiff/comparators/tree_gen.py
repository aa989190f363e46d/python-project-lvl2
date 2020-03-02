from gendiff.diff_structure.tree import make_tree, add_altered, add_removed, \
                                        add_added, add_intact, add_nested
from typing import Mapping


def generate_diff_tree(old_tree_map, new_tree_map):
    old_keys, new_keys = old_tree_map.keys(), new_tree_map.keys()
    diff = make_tree()
    for k in old_keys & new_keys:
        old_val, new_val = old_tree_map[k], new_tree_map[k]
        if not (isinstance(old_val, Mapping) and isinstance(new_val, Mapping)):
            if old_val == new_val:
                add_intact(diff, k, old_val)
            else:
                add_altered(diff, k, old_val, new_val)
        else:
            add_nested(diff, k, generate_diff_tree(old_val, new_val))
    for k in new_keys - old_keys:
        add_added(diff, k, new_tree_map[k])
    for k in old_keys - new_keys:
        add_removed(diff, k, old_tree_map[k])
    return diff
