import os
import sys
import argparse

PEP8 = 'pep8 '
PATH_PLUGIN_DIR = 'src/plugins/'
TAIL_PEP8 = '/*.py'
FORMAT = ' --format='
DEFAULT = 'default'
NAME_CHECKER = 'checker'
PYLINT_CHECK_FUNCTIONS = " pylint --disable=all --reports=n --load-plugins " \
    + NAME_CHECKER + ' '
PYLINT_CHECK_FILE = "pylint --disable=all --enable=F0001  --reports=n "
MAIN = '/main.py'
INIT = '/__init__.py'
PYTHONPATH = 'PYTHONPATH='
num_error = 0
TEXT_GOOD = 'No config file found, using default configuration\n'


def make_reqpep8(name_plugin, type_format):
    global num_error
    str_pep8 = PEP8 + PATH_PLUGIN_DIR + \
        unicode(name_plugin) + TAIL_PEP8 + FORMAT + type_format
    data = os.popen(str_pep8).read()
    if len(data) > 0:
        print data
        num_error = 1
    print 'Error code: ' + unicode(num_error)
    sys.exit(unicode(num_error))


def checker_pylint(name_plugin):
    global num_error
    STR_PYLINT_FILE_MAIN = PYLINT_CHECK_FILE + \
        PATH_PLUGIN_DIR + str(name_plugin) + MAIN
    STR_PYLINT_FILE_INIT = PYLINT_CHECK_FILE + \
        PATH_PLUGIN_DIR + str(name_plugin) + INIT
    STR_PYLINT_FUNCTIONS_FIND = PYTHONPATH + sys.path[0] + \
        PYLINT_CHECK_FUNCTIONS + PATH_PLUGIN_DIR + str(name_plugin) + MAIN
    data_init = os.popen(STR_PYLINT_FILE_INIT).read()
    if len(data_init) != 0:
        num_error = 1
        print data_init
    data_main = os.popen(STR_PYLINT_FILE_MAIN).read()
    if len(data_main) == 0:
        data_pylint_main = os.popen(STR_PYLINT_FUNCTIONS_FIND).read()
        if len(data_pylint_main) != 0:
            num_error = 1
            print data_pylint_main
    else:
        num_error = 1
        print data_main


def run():
    parser = argparse.ArgumentParser(description='Validate plugins')
    parser.add_argument('name', help='Name plugin')
    parser.add_argument('type_format', nargs='?',
                        default=DEFAULT, type=str, help='Type format')
    args = parser.parse_args()
    make_reqpep8(args.name, args.type_format)
    checker_pylint(args.name)
    print 'Error code: ' + str(num_error)
    sys.exit(str(num_error))
if __name__ == '__main__':
    run()
