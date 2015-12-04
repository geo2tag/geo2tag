from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException


class MetadataListResource(Resource):

    @possibleException
    def get(self):
        list_args = parseGetParameters()
        

    @possibleException
    def post(self):
        pass
