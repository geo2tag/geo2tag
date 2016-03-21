import os
import sys
import argparse
import subprocess
from datetime import datetime

DOCKERFILE = 'dockerfile'
SETUP_PIP_DEPENDENCIES = 'scripts/setup_pip_dependencies.sh'
REQUREMENTS = 'scripts/requirements.txt'
BUILD_DOCKER = './scripts/docker_build.sh'
STR_DOCKER_IMG = 'docker images --format "{{.CreatedAt}}" '

def getDateImage(name_img):
    str_dockerimg = STR_DOCKER_IMG + name_img
    date = subprocess.Popen(str_dockerimg,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    res = date.communicate()
    resdate = datetime.strptime(res[0][0:19], "%Y-%m-%d %H:%M:%S")
    return resdate


def getDateEditFile(path_file):
    sec = os.path.getmtime(path_file)
    return datetime.fromtimestamp(sec)


def compDate(date1, date2):
    if date1 > date2:
        return True
    else:
        return False


def buildImage(date_img):
    date1 = getDateEditFile(DOCKERFILE)
    date2 = getDateEditFile(SETUP_PIP_DEPENDENCIES)
    date3 = getDateEditFile(REQUREMENTS)
    num_code = 0
    if compDate(date1, date_img) or compDate(date2, date_img) or \
       compDate(date3, date_img):
        print 'Start build'
        os.system(BUILD_DOCKER)
        print 'Date image: ' + str(date_img)
        print 'Date dockefile: ' + str(date1)
        print 'Date setup_pip_dependencies.sh: ' + str(date2)
        print 'Date requirements.txt ' + str(date3)
        num_code = 1
    else:
        print 'It does not require rebuilding'
        print 'Date image: ' + str(date_img)
        print 'Date dockefile: ' + str(date1)
        print 'Date setup_pip_dependencies.sh: ' + str(date2)
        print 'Date requirements.txt: ' + str(date3)
        num_code = 0
    sys.exit(num_code)


def run():
    parser = argparse.ArgumentParser(description='Auto build image docker')
    parser.add_argument('--name', help='Name image')
    args = parser.parse_args()
    if args.name is not None:
        date0 = getDateImage(args.name)
        buildImage(date0)
    else:
        print 'No argument image'

if __name__ == '__main__':
    run()
