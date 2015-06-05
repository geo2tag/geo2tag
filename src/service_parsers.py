from flask_restful import reqparse

ARGS_LOG_SIZE = "logSize"

class ServiceParser():
    @staticmethod
    def parsePutParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(ARGS_LOG_SIZE, type=int, required=True)
        args = parser.parse_args()
        return args