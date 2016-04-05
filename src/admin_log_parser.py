from flask_restful import reqparse

SUBSTRING = 'substring'
NUMBER = 'number'
OFFSET = 'offset'


class AdminLogParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(SUBSTRING, type=unicode)
        parser.add_argument(NUMBER, type=int)
        parser.add_argument(OFFSET, type=int)
        args = parser.parse_args()
        return args
