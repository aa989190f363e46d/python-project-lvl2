from gendiff.diff_structure.tree import dump_tree
from yaml import dump


def format_diff(diff_tree):
    return dump({'diff': dump_tree(diff_tree)})
