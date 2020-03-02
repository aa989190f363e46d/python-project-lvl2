from gendiff.diff_structure.tree import dump_tree
from json import dumps


def format_diff(diff_tree):
    return dumps({'diff': dump_tree(diff_tree)})
