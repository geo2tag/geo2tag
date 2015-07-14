import os
import sys
import argparse
sys.path.append('../')


FILE_NAME = 'test_'
INCLUDE_MODULE = 'import unittest\nimport sys\nsys.path.append(' + "'../'" + ')\nfrom db_model import getDbObject\n\n'
TAB = '    '

def generateUnittest(args):
    os.chdir('src/tst')
    unittestFile = open(FILE_NAME + args.name + '.py', 'w')
    unittestFile.write(INCLUDE_MODULE)
    className = checkFileName(args.name)
    unittestFile.write('class Test' + className + '(unittest.TestCase):\n')
    unittestFile.write(TAB + 'def test' + className + '(self):\n\n')
    unittestFile.write(TAB + '@classmethod\n' + TAB + 'def setUpClass(cls):\n\n')
    unittestFile.write(TAB + '@classmethod\n' + TAB + 'def tearDownClass(cls):\n\n')

def run():
    parser = argparse.ArgumentParser(description='Generate unittest')
    parser.add_argument('--name', help='enter unittest name', required=True)
    args = parser.parse_args()
    generateUnittest(args)
    print ("Success. File created. File - /src/tst/" + FILE_NAME + args.name + '.py')

def checkFileName(FileName):
    i = FileName.find('_')
    FileName = FileName.capitalize()
    while i != -1:
        FileName = FileName[0:i] + FileName[i+1:].capitalize()
        i = FileName.find('_')
    return FileName

if __name__ == '__main__':
    run()
