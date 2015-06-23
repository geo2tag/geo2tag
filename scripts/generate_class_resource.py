import os
METHODS = ['post', 'get', 'put', 'delete']

INCLUDE_MODULE = 'from flask_restful import reqparse\n\
from flask.ext.restful import Resource\n\n'
INCLUDE_MODULE_PARSER = 'from flask_restful import reqparse\n\n'
STATIC = '@staticmethod\n'
PARSER_TEMPLETE = 'parser = reqparse.RequestParser()'
TAB = '    '
DEF = 'def '
def make_generator(args):
    print args.m
    if args.m is None or args.name is None:
        parser.print_help()
        return
    for method in args.m:
        if method.lower() not in METHODS:
            print 'method ' + method + ' not in ' + str(METHODS)
            return

    fileName = args.name + '.py'
    os.chdir('../src')
    newResource = open(fileName, 'w')
    newResource.write(INCLUDE_MODULE)
    newResource.write('class ' + args.name + '(Resource):\n')
    for methods in args.m:
        newResource.write(TAB + DEF + methods.lower() + '():\n')
        newResource.write(TAB + TAB + '\n')

    fileNameParser = args.name + '_parser.py'
    newParser = open(fileNameParser, 'w')
    newParser.write(INCLUDE_MODULE_PARSER)
    newParser.write('class ' + args.name  + 'Parser():\n')
    for methods in args.m:
        newParser.write(TAB + STATIC)
        newParser.write(TAB + DEF + 'parse' + methods[0].upper() + methods[1::].lower() + 'Parameters' + '():\n')
        newParser.write(TAB + TAB + PARSER_TEMPLETE + '\n')
        newParser.write(TAB + TAB + '\n')


import argparse
parser = argparse.ArgumentParser(description='Generate class resourse')
parser.add_argument('--name', help='enter name of resourse class', required=True)
parser.add_argument('--m', type = str, help='enter methods of resourse class', required=True, nargs = '+')
args = parser.parse_args()
print args
make_generator(args)
