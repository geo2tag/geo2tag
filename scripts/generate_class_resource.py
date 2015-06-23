import os
METHODS = ['post', 'get', 'put', 'delete']

INCLUDE_MODULE = 'from flask_restful import reqparse\n\
from flask.ext.restful import Resource\n\n'
TAB = '    '
DEF = 'def '
def make_generator(args):
    print args.m
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


import argparse
parser = argparse.ArgumentParser(description='Generate class resourse')
parser.add_argument('--name', help='enter name of resourse class', required=True)
parser.add_argument('--m', type = str, help='enter methods of resourse class', required=True, nargs = '+')
args = parser.parse_args()
print args
make_generator(args)
