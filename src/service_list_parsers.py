from flask_restful import reqparse

GET_ARGS_NUMBER = "number"
GET_ARGS_OFFSET = "offset"
POST_ARGS_NAME = "name"
POST_ARGS_LOG_SIZE = "logSize"
POST_ARGS_OWNER_ID = "ownerId"
DEFAULT_OWNER_ID = "STUB"


class ServiceListParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(GET_ARGS_NUMBER, type=int, default=None)
        parser.add_argument(GET_ARGS_OFFSET, type=int, default=None)
        args = parser.parse_args()
        return args

    @staticmethod
    def parsePostParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(POST_ARGS_NAME, type=unicode, required=True)
        parser.add_argument(POST_ARGS_LOG_SIZE, type=int, default=1048576)
        parser.add_argument(POST_ARGS_OWNER_ID, type=unicode,
                            default=DEFAULT_OWNER_ID)
        args = parser.parse_args()
        return args
