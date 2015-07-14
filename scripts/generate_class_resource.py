import os
import sys
sys.path.append('../')
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
GET_PATH_FUNC = "getPathWithPrefix('"
MAIN_STR = "if __name__ == '__main__':\n"
addResource = 'api.add_resource('
MAIN_FILE = 'main.py'
PARSER_ARGS = {}

def make_generator(args):
    className = checkFileName(args.name)
    IMPORT_RESOURCE = 'from ' + args.name + ' import ' + className + '\n'
    if args.m is None or args.name is None:
        parser.print_help()
        return
    for method in args.m:
        if method.lower() not in METHODS:
            print 'method ' + method + 'not in ' + str(METHODS)
            return

    fileName = args.name + '.py'
    os.chdir('src')
    newResource = open(fileName, 'w')
    newResource.write(INCLUDE_MODULE)
    newResource.write('class ' + className + '(Resource):\n')

    for methods in args.m:
        newResource.write(TAB + DEF + methods.lower() + '(self):\n')
        newResource.write(TAB + TAB + 'pass\n')
        PARSER_ARGS[methods] = {}

    main = open(MAIN_FILE, 'r')
    mainStrings = main.readlines()
    mainWrite = open(MAIN_FILE, 'w')
    if MAIN_STR not in mainStrings:
        print 'file main.py has invalid format'
        return

    mainWrite.write(IMPORT_RESOURCE)
    for string in mainStrings:
        if MAIN_STR != string:
            mainWrite.write(string)
        else:
            mainWrite.write(addResource + className + ', ' + GET_PATH_FUNC + args.url + "\'))\n")
            mainWrite.write(MAIN_STR)
    print 'Resourse added successfully'

    flag = True
    i = 0
    while flag:
        while i < len(args.m):
            countArgs = int(input('Enter count of arguments by method ' + args.m[i] + ' '))
            j = 0
            while j < countArgs:
                print 'Method ' + str(args.m[i]) + ' argument ' + str(j + 1)
                argument = sys.stdin.readline()
                argumentDict = argument.split(' ')
                if argumentDict[1][0:-1] in TYPES:
                    PARSER_ARGS[args.m[i]][argumentDict[0].lower()] = argumentDict[1][0:-1]
                    j+=1
            i+=1
        flag = False

    print PARSER_ARGS

    fileNameParser = args.name + '_parser.py'
    newParser = open(fileNameParser, 'w')
    newParser.write(INCLUDE_MODULE_PARSER)
    newParser.write('class ' + className + 'Parser():\n')
    i = 0
    for methods in args.m:
        newParser.write(TAB + STATIC)
        newParser.write(TAB + DEF + 'parse' + methods[0].upper() + methods[1::].lower() + 'Parameters' + '():\n')
        newParser.write(TAB + TAB + PARSER_TEMPLETE + '\n')
        for arg in PARSER_ARGS[methods]:
            newParser.write(TAB + TAB + ADD_ARGUMENT + arg + ', type = ' + PARSER_ARGS[methods][arg] + ')\n')
        newParser.write(TAB + TAB + '\n')
        i+=1

def run():
    import argparse
    parser = argparse.ArgumentParser(description='Generate class resourse')
    parser.add_argument('--name', help='enter name of resourse class', required=True)
    parser.add_argument('--m', type = str, help='enter methods of resourse class', required=True, nargs = '+')
    parser.add_argument('--url', type=str, help='enter url of resourse', required=True)
    args = parser.parse_args()
    make_generator(args)

def checkFileName(FileName):
    i = FileName.find('_')
    FileName = FileName.capitalize()
    while i != -1:
        FileName = FileName[0:i] + FileName[i+1:].capitalize()
        i = FileName.find('_')
    return FileName

if __name__ == '__main__':
    run()