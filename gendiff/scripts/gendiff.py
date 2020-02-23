from gendiff.cli.posix import get_args
from gendiff.parsers.parser_selector import select
from gendiff.comparators.plain_map import generate_diff


def main():
    parsed_args = get_args()
    first_parser = select(parsed_args.first_file)
    second_parser = select(parsed_args.second_file)
    print(generate_diff(
        first_parser(parsed_args.first_file),
        second_parser(parsed_args.second_file)))


if __name__ == "__main__":
    main()
