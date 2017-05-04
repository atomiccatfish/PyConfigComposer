__author__ = 'Richard McAllister'

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='command', help='')

    a_subparser = subparsers.add_parser('a_subparser')
    a_subparser.add_argument('-f', dest='config_file', action='store', help='Full path of the config file.',
                             required=True)

    a_sub_sub_parser = a_subparser.add_subparsers(dest='sub_command')

    args = parser.parse_args()

    if args.command == '':
        pass