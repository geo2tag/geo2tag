from flask_restful import Resource
from possible_exception import possibleException
from user_list_resource_parser import UserListResourceParser, \
    GET_ARGS_NUMBER, GET_ARGS_OFFSET, GET_ARGS_LOGIN
from user_routines import findUsers


class UserListResource(Resource):

    @possibleException
    def get(self):
        params = UserListResourceParser.parseGetParameters()
        users = findUsers(params[GET_ARGS_NUMBER], params[GET_ARGS_OFFSET],
                          params[GET_ARGS_LOGIN])
        return users
