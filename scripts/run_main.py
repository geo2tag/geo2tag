import argparse
import os

READ_FILE_PATH = 'scripts/'
PYTHONPATH = 'PYTHONPATH='
SRC = '/src'
PYTHON_MAIN = ' python main.py'


def creat_path(name_file):
    try:
        f = open(READ_FILE_PATH + name_file, 'r')
        path_file_in_src = f.read()
        this_path = os.getcwd() + SRC
        PATH = this_path + path_file_in_src
        run_main(PATH)
    except Exception:
        print 'No file config for PYTHONPATH'


def run_main(PATH):
    os.chdir('src/')
    RUN = PYTHONPATH + PATH + PYTHON_MAIN
    print RUN
    os.system(RUN)


def run():
    parser = argparse.ArgumentParser(description='Run main.py script')
    parser.add_argument('name', help='Name file config for PYTHONPATH')
    args = parser.parse_args()
    creat_path(args.name)

if __name__ == '__main__':
    run()
