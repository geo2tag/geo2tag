import os
import sys
import subprocess

PEP8 = 'pep8 '
PATH_PLUGIN_DIR = 'src/plugins/'
TAIL_PEP8 = '/*.py'
FORMAT = ' --format='
DEFAULT = 'default'

def make_reqpep8(name_plugin,type_format):
    num_error = 0
    str_pep8 = PEP8 + PATH_PLUGIN_DIR + str(name_plugin) + TAIL_PEP8 + FORMAT + type_format
    data = os.popen(str_pep8).read()
    if len(data) > 0:
    	print data
    	num_error = 1
    print 'Error code: ' + str(num_error)
    return num_error

def run():
    
    if len(sys.argv) == 1:
        print 'No argument: plugin name.'

    if len(sys.argv) == 2:
    	name_plugin = sys.argv[1]
        make_reqpep8(name_plugin, DEFAULT)
    if len(sys.argv) == 3:
    	name_plugin = sys.argv[1]
    	type_format = sys.argv[2]
    	make_reqpep8(name_plugin, type_format)
if __name__ == '__main__':
    run()
