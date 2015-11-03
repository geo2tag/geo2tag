import os
import sys
import argparse
import subprocess

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
TEXT_GOOD = 'No config file found, using default configuration\n'


def make_reqpep8(name_plugin, type_format):
    num_error = 0
    str_pep8 = PEP8 + PATH_PLUGIN_DIR + \
        unicode(name_plugin) + TAIL_PEP8 + FORMAT + type_format
    process = subprocess.Popen(str_pep8,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if len(stdout) > 0 or len(stderr) > 0:
        num_error = 1
    print("stdout='{}'\nstderr='{}'".format(stdout, stderr))
    sys.exit(unicode(num_error))


def checker_pylint(name_plugin, num_error):
    STR_PYLINT_FILE_MAIN = PYLINT_CHECK_FILE + \
        PATH_PLUGIN_DIR + str(name_plugin) + MAIN
    STR_PYLINT_FILE_INIT = PYLINT_CHECK_FILE + \
        PATH_PLUGIN_DIR + str(name_plugin) + INIT
    STR_PYLINT_FUNCTIONS_FIND = PYTHONPATH + sys.path[0] + \
        PYLINT_CHECK_FUNCTIONS + PATH_PLUGIN_DIR + str(name_plugin) + MAIN
    data_init = subprocess.Popen(STR_PYLINT_FILE_INIT,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
    stdout, stderr = data_init.communicate()
    if len(stdout) > 0 or len(stderr) > 0:
        num_error = 1
    print("stdout='{}'\nstderr='{}'".format(stdout, stderr))
    data_main = subprocess.Popen(STR_PYLINT_FILE_MAIN,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
    stdout, stderr = data_main.communicate()
    print("stdout='{}'\nstderr='{}'".format(stdout, stderr))
    if len(stdout) == 0 and len(stderr) == 0:
        data_pylint_main = os.popen(STR_PYLINT_FUNCTIONS_FIND).read()
        if len(stdout) > 0 or len(stderr) > 0:
            num_error = 1
            print data_pylint_main
    else:
        num_error = 1
        print data_main
    return num_error
    print 'Error code: ' + str(num_error)
    sys.exit(str(num_error))


def run():
    parser = argparse.ArgumentParser(description='Validate plugins')
    parser.add_argument('-name', help='Name plugin')
    parser.add_argument('-type_format', nargs='?',
                        default=DEFAULT, type=str, help='Type format')
    args = parser.parse_args()
    num_error = make_reqpep8(args.name, args.type_format)
    checker_pylint(args.name, num_error)

if __name__ == '__main__':
    run()
