import flask_restful as restful
from flask_restful import Resource
import os

# Considering that we are in src dir
DEBUG_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/DEBUG"


def getDebugInfo():
    file_defuginfo = open(DEBUG_FILE_PATH, 'r')
    print DEBUG_FILE_PATH
    listFileData = file_defuginfo.readlines()
    return ''.join(listFileData)


class DebugInfoResource(Resource):

    def get(self):
        return getDebugInfo()
