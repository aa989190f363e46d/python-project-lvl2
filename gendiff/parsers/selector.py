from os.path import splitext


def load_json_parser():
    from gendiff.parsers.json import parse
    return parse


def load_yaml_parser():
    from gendiff.parsers.yaml import parse
    return parse


PARSERS_DICT = {'.yml': load_yaml_parser,
                '.yaml': load_yaml_parser,
                '.json': load_json_parser}


def select(file):
    _, ext = splitext(file.name)
    return PARSERS_DICT[ext]()
