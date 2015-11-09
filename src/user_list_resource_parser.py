from flask_restful import reqparse


GET_ARGS_NUMBER = 'number'
GET_ARGS_OFFSET = 'offset'
GET_ARGS_LOGIN = 'login'


class UserListResourceParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(GET_ARGS_NUMBER, type=int, required=True)
        parser.add_argument(GET_ARGS_OFFSET, type=int, required=True)
        parser.add_argument(GET_ARGS_LOGIN, type=unicode, required=True)
        args = parser.parse_args()
        return args
