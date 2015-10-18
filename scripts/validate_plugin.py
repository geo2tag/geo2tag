import os
import sys
import subprocess

PEP8 = 'pep8 '
PATH_PLUGIN_DIR = 'src/plugins/'
TAIL_PEP8 = '/*.py'
FORMAT = ' --format='
DEFAULT = 'default'
PYLINT_CHECK_FUNCTIONS = "pylint --disable=all --enable=C0103  \
    --function-rgx='(([a-z]*)|(getPluginResources)|(getPluginInfo))$' --reports=n "
PYLINT_CHECK_FILE = "pylint --disable=all --enable=F0001  --reports=n "
MAIN = '/main.py'
INIT = '/__init__.py'


def make_reqpep8(name_plugin, type_format):
    num_error = 0
    str_pep8 = PEP8 + PATH_PLUGIN_DIR + \
        str(name_plugin) + TAIL_PEP8 + FORMAT + type_format
    data = os.popen(str_pep8).read()
    if len(data) > 0:
        print data
        num_error = 1
    print 'Error code: ' + str(num_error)
    return num_error


def checker_pylint(name_plugin):
    STR_PYLINT_FILE_MAIN = PYLINT_CHECK_FILE + \
        PATH_PLUGIN_DIR + str(name_plugin) + MAIN
    STR_PYLINT_FILE_INIT = PYLINT_CHECK_FILE + \
        PATH_PLUGIN_DIR + str(name_plugin) + INIT
    STR_PYLINT_FUNCTIONS_FIND = PYLINT_CHECK_FUNCTIONS + \
        PATH_PLUGIN_DIR + str(name_plugin) + MAIN
    data = os.popen(STR_PYLINT_FILE_INIT).read()
    if len(data) != 0:
        print data
    data = os.popen(STR_PYLINT_FILE_MAIN).read()
    if len(data) == 0:
        print data
        data = os.popen(STR_PYLINT_FUNCTIONS_FIND).read()
        if len(data) != 0:
            print data


def run():

    if len(sys.argv) == 1:
        print 'No argument: plugin name.'

    if len(sys.argv) == 2:
        name_plugin = sys.argv[1]
        make_reqpep8(name_plugin, DEFAULT)
        checker_pylint(name_plugin)
    if len(sys.argv) == 3:
        name_plugin = sys.argv[1]
        type_format = sys.argv[2]
        make_reqpep8(name_plugin, type_format)
        checker_pylint(name_plugin)
if __name__ == '__main__':
    run()
