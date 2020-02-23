from argparse import ArgumentParser, FileType

FROMATS_LIST = ['plain', 'json', 'yaml']


def get_args():
    parser = ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=FileType('r'),
                        help='conventionaly old file')
    parser.add_argument('second_file', type=FileType('r'),
                        help='conventionaly new file')
    fmt_hlp_str = ("output format (one of {{{}}}, %(default)s"
                   " if omitted)").format(','.join(FROMATS_LIST))
    parser.add_argument('-f', '--format', type=str,
                        nargs='?', default='plain',
                        metavar='FORMAT',
                        help=fmt_hlp_str)
    return parser.parse_args()
