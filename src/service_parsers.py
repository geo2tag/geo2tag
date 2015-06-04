from flask_restful import reqparse

class ServiceParser():
    @staticmethod
    def parsePutParameters():
        parser = reqparse.RequestParser()
        parser.add_argument('logSize', type=int, required=True)
        args = parser.parse_args()
        return args

class ServiceListParser():
    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument('number', type=int, default=None)
        parser.add_argument('offset', type=int, default=None)
        args = parser.parse_args()
        return args

    @staticmethod
    def parsePostParameters():
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('logSize', type=int, default=1048576)
        parser.add_argument('ownerId', type=str, default='STUB')
        args = parser.parse_args()
        return args