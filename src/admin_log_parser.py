from flask_restful import reqparse

SUBSTRING = 'substring'
NUMBER = 'number'
OFFSET = 'offset'
SERVICE = 'service_name'
DATE_FROM = 'date_from'
DATE_TO = 'date_to'


class AdminLogParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(SUBSTRING, type=unicode)
        parser.add_argument(NUMBER, type=int)
        parser.add_argument(OFFSET, type=int)
        parser.add_argument(SERVICE, type=unicode)
        parser.add_argument(
            DATE_FROM, type=date_utils.datetime_from_iso8601, default=None)
        parser.add_argument(
            DATE_TO, type=date_utils.datetime_from_iso8601, default=None)
        args = parser.parse_args()
        return args
