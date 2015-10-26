import os
import sys
import argparse


PEP8 = 'pep8 '
PATH_PLUGIN_DIR = 'src/plugins/'
TAIL_PEP8 = '/*.py'
FORMAT = ' --format='
DEFAULT = 'default'


def make_reqpep8(name_plugin, type_format):
    num_error = 0
    str_pep8 = PEP8 + PATH_PLUGIN_DIR + \
        str(name_plugin) + TAIL_PEP8 + FORMAT + type_format
    data = os.popen(str_pep8).read()
    if len(data) > 0:
        print data
        num_error = 1
    print 'Error code: ' + str(num_error)
    sys.exit(str(num_error))


def run():
    parser = argparse.ArgumentParser(description='Validate plugins')
    parser.add_argument('-name', help='Name plugin')
    parser.add_argument('-type_format', nargs='?',
                        default=DEFAULT, type=str, help='Type format')
    args = parser.parse_args()
    make_reqpep8(args.name, args.type_format)
if __name__ == '__main__':
    run()
