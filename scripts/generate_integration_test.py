import os
import sys
import argparse
sys.path.append('../')


FILE_NAME = 'test_'
INCLUDE_MODULE = "import unittest\nimport requests\nfrom basic_integration_test import BasicIntegrationTest\n\nTEST_URL = ''\nVALID_RESPONSE_CODE = 200\n\n"
TAB = '    '
MAIN_FILE = 'main.py'
MAIN_STRING = 'from basic_integration_test import BasicIntegrationTest\n'
MAIN_STRING2 = '    suite = unittest.TestSuite()\n'

def generateIntegrationTest(args):
    os.chdir('src/tst_integration')
    unittestFile = open(FILE_NAME + args.name + '.py', 'w')
    unittestFile.write(INCLUDE_MODULE)
    unittestFile.write('class Test' + args.name + '(BasicIntegrationTest):\n')
    unittestFile.write(TAB + 'def test' + args.name + '(self):\n')
    unittestFile.write(TAB + TAB + 'response = requests.get(self.getUrl(TEST_URL))')
    mainFile = open(MAIN_FILE, 'r')
    mainStrings = mainFile.readlines()
    mainFile.close()
    mainFile = open(MAIN_FILE, 'w')
    for string in mainStrings:
        if MAIN_STRING == string:
            mainFile.write(string)
            mainFile.write('from ' + FILE_NAME + args.name + ' import Test' + args.name + '\n')
        if MAIN_STRING2 == string:
            mainFile.write(string)
            mainFile.write(TAB + 'suite.addTest(BasicIntegrationTest.parametrize(Test' + args.name + ', param=host))\n')
        else:
            mainFile.write(string)
    

def run():
    parser = argparse.ArgumentParser(description='Generate unittest')
    parser.add_argument('--name', help='enter unittest name', required=True)
    args = parser.parse_args()
    generateIntegrationTest(args)
    print ("Success. File created. File - /src/tst_integration/" + FILE_NAME + args.name + '.py')

if __name__ == '__main__':
    run()