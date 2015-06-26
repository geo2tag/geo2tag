import os
import sys
import argparse
sys.path.append('../')


FILE_NAME = 'test_'
INCLUDE_MODULE = 'import unittest\nimport sys\nfrom pymongo import MongoClient\nsys.path.append(' + "'../'" + ')\n\n'
TAB = '    '

def generateUnittest(args):
	os.chdir('../src/tst')
	unittestFile = open(FILE_NAME + args.name + '.py', 'w')
	unittestFile.write(INCLUDE_MODULE)
	unittestFile.write('class Test' + args.name + '(unittest.TestCase):\n')
	unittestFile.write(TAB + 'def test' + args.name + '(self):\n\n')
	unittestFile.write(TAB + '@classmethod\n' + TAB + 'def setUpClass(cls):\n\n')
	unittestFile.write(TAB + '@classmethod\n' + TAB + 'def tearDownClass(cls):\n\n')

def run():
	parser = argparse.ArgumentParser(description='Generate unittest')
	parser.add_argument('--name', help='enter unittest name', required=True)
	args = parser.parse_args()
	generateUnittest(args)

if __name__ == '__main__':
    run()