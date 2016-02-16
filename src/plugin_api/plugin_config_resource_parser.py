from flask_restful import request
from json import loads


class PluginConfigResourceParser():

    @staticmethod
    def parsePostParameters():
        print request.get_data()
        print loads(request.get_data())
        args = loads(request.get_data())
        return args
