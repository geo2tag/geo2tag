from flask_restful import reqparse

ARGS_SUBSTRING = 'substring'
ARGS_NUMBER = 'number'
ARGS_OFFSET = 'offset'

class ChannelsListResourceParser():
    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_SUBSTRING, type=str)
        parser.add_argument(ARGS_NUMBER, type=int)
        parser.add_argument(ARGS_OFFSET, type=int)
        args = parser.parse_args()
        return args