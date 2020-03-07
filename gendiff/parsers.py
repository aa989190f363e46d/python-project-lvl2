import json
import yaml


parse_json = json.load


def parse_yaml(path_to_file):
    return yaml.load(path_to_file.read(), Loader=yaml.SafeLoader)
