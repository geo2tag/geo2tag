from flask_restful import reqparse
from flask import request
from json import loads

ARGS_NUMBER = 'number'
ARGS_OFFSET = 'offset'
ARGS_QUERY = 'query'


class MetadataListResourceParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_NUMBER, type=int, required=True)
        parser.add_argument(ARGS_OFFSET, type=int, required=True)
        parser.add_argument(ARGS_QUERY, type=unicode)
        args = parser.parse_args()
        args[ARGS_QUERY] = loads(args[ARGS_QUERY])
        return args

    @staticmethod
    def parsePostParameters():
        return request.get_json(force=True)
