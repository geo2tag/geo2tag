from flask_restful import reqparse

ARGS_SUBSTRING = 'substring'
ARGS_NUMBER = 'number'
ARGS_OFFSET = 'offset'
ARGS_NAME = 'name'
ARGS_JSON = 'json'

class ChannelsListResourceParser():
    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_SUBSTRING, type=str)
        parser.add_argument(ARGS_NUMBER, type=int)
        parser.add_argument(ARGS_OFFSET, type=int)
        args = parser.parse_args()
        return args

    @staticmethod
    def parsePostParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_NAME, type=str, required=True)
        parser.add_argument(ARGS_JSON, type=str, required=True)
        args = parser.parse_args()
        return args