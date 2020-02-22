from json import load

FSTR = '{} "{}": {}'


def generate_diff(path_to_file1, path_to_file2):
    changes_list = []
    json_old = load(path_to_file1)
    json_new = load(path_to_file2)
    keys_old = set(json_old.keys())
    keys_new = set(json_new.keys())
    appended = keys_new - keys_old
    preserved = keys_new & keys_old
    for k in sorted(preserved):
        old_val, new_val = json_old[k], json_new[k]
        if old_val == new_val:
            changes_list.append(
                FSTR.format(' ', k, old_val))
        else:
            changes_list.extend([
                FSTR.format('-', k, old_val),
                FSTR.format('+', k, new_val)])
    changes_list.extend(
        [FSTR.format('+', k, json_new[k]) for k in sorted(appended)])
    removed = keys_old - keys_new
    changes_list.extend(
        [FSTR.format('-', k, json_old[k]) for k in sorted(removed)])
    return '{{\n  {}\n}}'.format('\n  '.join(changes_list))
