from flask_restful import reqparse

ARGS_JSON = 'json'


class MetadataParser():

    @staticmethod
    def parsePutParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_JSON, type=unicode, required=True)
        args = parser.parse_args()
        return args
