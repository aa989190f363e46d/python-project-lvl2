FSTR = '{} "{}": {}'


def generate_diff(old_map, new_map):
    changes_list = []
    keys_old = set(old_map.keys())
    keys_new = set(new_map.keys())
    appended = keys_new - keys_old
    preserved = keys_new & keys_old
    for k in preserved:
        old_val, new_val = old_map[k], new_map[k]
        if old_val == new_val:
            changes_list.append(
                FSTR.format(' ', k, old_val))
        else:
            changes_list.extend([
                FSTR.format('-', k, old_val),
                FSTR.format('+', k, new_val)])
    changes_list.extend(eval_changes('+', appended, new_map))
    removed = keys_old - keys_new
    changes_list.extend(eval_changes('-', removed, old_map))
    return '{{\n  {}\n}}'.format('\n  '.join(changes_list))


def eval_changes(prefix_mark, changes, source):
    '''For better  code climate.

    CC needed for remove any
    suspicious duplication
    '''
    return [FSTR.format(prefix_mark, k, source[k]) for k in changes]
