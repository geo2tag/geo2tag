import os
METHODS = ['post', 'get', 'put', 'delete']
TYPES = ['bool', 'int', 'float', 'tuple', 'list', 'str', 'dict', 'set']
INCLUDE_MODULE = 'from flask_restful import reqparse\n\
from flask.ext.restful import Resource\n\n'
INCLUDE_MODULE_PARSER = 'from flask_restful import reqparse\n\n'
STATIC = '@staticmethod\n'
PARSER_TEMPLETE = 'parser = reqparse.RequestParser()'
ADD_ARGUMENT = 'parser.add_argument('
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

    for i in range(len(args.p)):
        if i%2 == 0:
            print args.p[i]
            if args.p[i].lower() not in TYPES:
                print 'Type ' + args.p[i] + ' is not base type '
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

    fileNameParser = args.name + '_parser.py'
    newParser = open(fileNameParser, 'w')
    newParser.write(INCLUDE_MODULE_PARSER)
    newParser.write('class ' + args.name  + 'Parser():\n')
    i = 0
    for methods in args.m:
        newParser.write(TAB + STATIC)
        newParser.write(TAB + DEF + 'parse' + methods[0].upper() + methods[1::].lower() + 'Parameters' + '():\n')
        newParser.write(TAB + TAB + PARSER_TEMPLETE + '\n')
        newParser.write(TAB + TAB + ADD_ARGUMENT + args.p[i] + ', type = ' + args.p[i+1] + ')')
        newParser.write(TAB + TAB + '\n')
        i+=1


import argparse
parser = argparse.ArgumentParser(description='Generate class resourse')
parser.add_argument('--name', help='enter name of resourse class', required=True)
parser.add_argument('--m', type = str, help='enter methods of resourse class', required=True, nargs = '+')
parser.add_argument('--p', type = str, help='enter parameters of parser', required=True, nargs = '+')
args = parser.parse_args()
make_generator(args)
