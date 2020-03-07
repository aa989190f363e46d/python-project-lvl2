from os.path import splitext

from gendiff.parsers import parse_json, parse_yaml
from gendiff.cli import get_args
from gendiff.diff_tree import generate_diff


def get_parsed(file):
    _, ext = splitext(file.name)
    if ext in ['.json']:
        return parse_json(file)
    elif ext in ['.yaml', 'yml']:
        return parse_yaml(file)


def main():
    parsed_args = get_args()
    with open(parsed_args.first_path, 'r') as first_file:
        with open(parsed_args.second_path, 'r') as second_file:
            first_parsed = get_parsed(first_file)
            second_parsed = get_parsed(second_file)
    diff_tree = generate_diff(first_parsed, second_parsed)
    print(parsed_args.format(diff_tree))


if __name__ == "__main__":
    main()
