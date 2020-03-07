from argparse import ArgumentParser, ArgumentTypeError
from os.path import splitext

import gendiff.formatters.plain
import gendiff.formatters.json
import gendiff.formatters.yaml


OUTPUT_FROMATS_DICT = {'plain': gendiff.formatters.plain.format_diff,
                       'json': gendiff.formatters.json.format_diff,
                       'yaml': gendiff.formatters.yaml.format_diff}

INPUT_FILE_EXT_LIST = ['.json', '.yaml', '.yml']


def check_input_path(path):
    _, ext = splitext(path)
    if not ext:
        msg = "Can't recognise format of {}.".format(path)
        raise ArgumentTypeError(msg)
    if ext not in INPUT_FILE_EXT_LIST:
        msg = "'{}' input file format not supported.".format(ext)
        raise ArgumentTypeError(msg)
    return path


def get_formatter(format_name):
    if format_name not in OUTPUT_FROMATS_DICT:
        msg = "'{}' output format not supported.".format(format_name)
        raise ArgumentTypeError(msg)
    return OUTPUT_FROMATS_DICT[format_name]


def get_args():
    parser = ArgumentParser(description='Generate diff')
    parser.add_argument('first_path', type=check_input_path,
                        help='conventionaly old file')
    parser.add_argument('second_path', type=check_input_path,
                        help='conventionaly new file')
    fmt_hlp_str = ("output format (one of {{{}}}, %(default)s"
                   " if omitted)").format(','.join(OUTPUT_FROMATS_DICT.keys()))
    parser.add_argument('-f', '--format', type=get_formatter,
                        nargs='?', default='plain',
                        metavar='FORMAT',
                        help=fmt_hlp_str)
    return parser.parse_args()
