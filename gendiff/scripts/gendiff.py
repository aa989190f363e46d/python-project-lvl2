from gendiff.cli.posix import get_args
from gendiff.parsers.selector import select as select_parser
from gendiff.formatters.selector import select as select_formatter
from gendiff.comparators.tree_gen import generate_diff_tree as generate_diff


def main():
    parsed_args = get_args()
    first_parser = select_parser(parsed_args.first_file)
    second_parser = select_parser(parsed_args.second_file)
    diff_tree = generate_diff(
        first_parser(parsed_args.first_file),
        second_parser(parsed_args.second_file))
    formatter = select_formatter(parsed_args.format)
    print(formatter(diff_tree))


if __name__ == "__main__":
    main()
