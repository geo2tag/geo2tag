import os
METHODS = ['post', 'get', 'put', 'delete']

INCLUDE_MODULE = 'from flask_restful import reqparse\n\
from flask.ext.restful import Resource\n\n'
TAB = '    '
DEF = 'def '
MAIN_STR = "if __name__ == '__main__':\n"
addResource = 'api.add_resource('
MAIN_FILE = 'main.py'
def make_generator(args):
    if args.m is None or args.name is None:
        parser.print_help()
        return
    for method in args.m:
        if method.lower() not in METHODS:
            print 'method ' + method + 'not in ' + str(METHODS)
            return

    fileName = args.name + '.py'
    os.chdir('../src')
    newResource = open(fileName, 'w')
    newResource.write(INCLUDE_MODULE)
    newResource.write('class ' + args.name + '(Resource):\n')
    for methods in args.m:
    	newResource.write(TAB + DEF + methods.lower() + '():\n')
    	newResource.write(TAB + TAB + '\n')
    main = open(MAIN_FILE, 'r')
    mainStrings = main.readlines()
    mainWrite = open(MAIN_FILE, 'w')
    if MAIN_STR not in mainStrings:
        print 'file main.py has invalid format'
        return

    for string in mainStrings:
        if MAIN_STR != string:
            mainWrite.write(string)
        else:
            mainWrite.write(addResource + args.name + ')\n')
            mainWrite.write(MAIN_STR)
    print 'Resourse added successfully'

import argparse
parser = argparse.ArgumentParser(description='Generate class resourse')
parser.add_argument('--name', help='enter name of resourse class', required=True)
parser.add_argument('--m', type = str, help='enter methods of resourse class', required=True, nargs = '+')
args = parser.parse_args()
make_generator(args)
