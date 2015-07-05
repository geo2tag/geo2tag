from flask.ext.restful import Resource
import os

#Considering that we are in src dir
DEBUG_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/DEBUG"


def getDebugInfo() :
    file = open(DEBUG_FILE_PATH, 'r')
    print DEBUG_FILE_PATH
    listFileData = file.readlines()
    return ''.join(listFileData)

class DebugInfoResource(Resource) :
    def get(self) :
        return getDebugInfo()

