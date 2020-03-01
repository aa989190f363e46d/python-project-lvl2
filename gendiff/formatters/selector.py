def load_plain_formatter():
    from gendiff.formatters.plain import format_diff
    return format_diff


def load_json_formatter():
    from gendiff.formatters.json import format_diff
    return format_diff


def load_yaml_formatter():
    from gendiff.formatters.yaml import format_diff
    return format_diff


FORMATTERS_DICT = {'plain': load_plain_formatter,
                   'json': load_json_formatter,
                   'yaml': load_yaml_formatter}


def select(fmt):
    return FORMATTERS_DICT[fmt]()
