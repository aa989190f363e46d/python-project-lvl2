from json import load

FSTR = '{} "{}": {}'


def generate_diff(path_to_file1, path_to_file2):
    changes_list = []
    json_old = load(open('path_to_file1'))
    json_new = load(open('path_to_file2'))
    keys_old = set(json_old.keys())
    keys_new = set(json_new.keys())
    appended = keys_new - keys_old
    changes_list.extend(
        [FSTR.format('+', k, json_new[k]) for k in appended])
    removed = keys_old - keys_new
    changes_list.extend(
        [FSTR.format('-', k, json_old[k]) for k in removed])
    preserved = keys_new & keys_old
    for k in preserved:
        old_val, new_val = json_old[k], json_new[k]
        if old_val != new_val:
            changes_list.extend([
                FSTR.format('-', k, old_val),
                FSTR.format('+', k, new_val)])
    return '{{{}\n}}'.format('\n\t'.join(changes_list))
