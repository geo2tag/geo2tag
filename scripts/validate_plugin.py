import os
import sys
import argparse
import subprocess

PEP8 = 'pep8 '
PATH_PLUGIN_DIR = 'src/plugins/'
TAIL_PEP8 = '/*.py'
FORMAT = ' --format='
DEFAULT = 'default'


def make_reqpep8(name_plugin, type_format):
    num_error = 0
    str_pep8 = PEP8 + PATH_PLUGIN_DIR + \
        str(name_plugin) + TAIL_PEP8 + FORMAT + type_format
    process = subprocess.Popen(str_pep8, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout,stderr = process.communicate()
    if len(stdout) > 0 or len(stderr) > 0:
        num_error = 1
    print("stdout='{}'\nstderr='{}'".format(stdout, stderr))
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
