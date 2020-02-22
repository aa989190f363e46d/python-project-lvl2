from gendiff.cli.posix import get_args
from gendiff.comparators.json import generate_diff


def main():
    parsed_args = get_args()
    print(generate_diff(parsed_args.first_file, parsed_args.second_file))


if __name__ == "__main__":
    main()
