from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException

class ManagePluginsResource(Resource):
    @possibleException
    def get(self):
        pluginsDict = ManagePluginsParser.parseGetParameters()
        print pluginsDict, '1111111111111111111111111111'