from flask_restful import reqparse
from flask import request

ARGS_NUMBER = 'number'
ARGS_OFFSET = 'offset'
ARGS_QUERY = 'query'
ARGS_JSON = 'json'


class MetadataListResourceParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_NUMBER, type=int, required=True)
        parser.add_argument(ARGS_OFFSET, type=int, required=True)
        parser.add_argument(ARGS_QUERY, type=unicode)
        args = parser.parse_args()
        return args

    @staticmethod
    def parsePostParameters():
        return request.get_json(force=True)
