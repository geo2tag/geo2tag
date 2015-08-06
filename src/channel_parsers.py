from flask_restful import reqparse

ARGS_NAME = 'name'
ARGS_JSON = 'json'
ARGS_ACL = 'acl'


class ChannelResourceParser():

    @staticmethod
    def parsePutParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_NAME, type=str, required=True)
        parser.add_argument(ARGS_JSON, type=str)
        parser.add_argument(ARGS_ACL, type=int)
        args = parser.parse_args()
        return args
