import os
import sys

PEP8 = 'pep8 '
PATH_PLUGIN_DIR = 'src/plugins/'
TAIL_PEP8 = '/*.py'

def run():
	dir_plugin = sys.argv[1]
	str_pep8 = PEP8 + PATH_PLUGIN_DIR + str(dir_plugin) + TAIL_PEP8
	os.system(str_pep8)
if __name__ == '__main__':
    run()