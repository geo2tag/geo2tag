from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException
from UserListResourceParser import Userlistresourceparser
from user_routines import findUserById


GET_ARGS_LOGIN = "login"


class UserListResource(Resource):
    @possibleException
    def get(self):
        args = Userlistresourceparser.parseGetParameters()
        login = args[GET_ARGS_LOGIN]
        return findUserById(login)