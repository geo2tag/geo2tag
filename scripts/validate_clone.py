import re
import sys
import argparse
import subprocess

TAIL_CLONE = '*.py'
CLONEDIGGER = "clonedigger "
PATTERN = "Refining candidates... (.*) clones were found"
num_error = 0


def check_directory(name_directory):
    if name_directory[-1] != '/':
        name_directory = name_directory + "/"
    clone_digger_run(name_directory + TAIL_CLONE)


def check_file(name_file):
    clone_digger_run(name_file)


def clone_digger_run(name):
    global num_error
    process = subprocess.Popen(CLONEDIGGER + name,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)
    stdout, stderr = process.communicate()
    regx = re.findall(PATTERN, stdout)
    if len(stdout) > 0 or len(stderr) > 0:
        if int(regx[0]) == 0:
            num_error = 0
            print "Clone not found"
        else:
            num_error = 1
            print "Clone in you directory/file: " + name + \
                " equally " + regx[0]
            print "Check file output.html"


def run():
    parser = argparse.ArgumentParser(description='Validate Clone')
    parser.add_argument('--directory', help='Name directory')
    parser.add_argument('--file', help='Name file')
    args = parser.parse_args()
    if args.directory is not None:
        check_directory(args.directory)
    else:
        check_file(args.file)
    sys.exit(num_error)


if __name__ == '__main__':
    run()
