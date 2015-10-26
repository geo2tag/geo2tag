from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException
from UserListResourceParser import Userlistresourceparser
from user_routines import findUserById


class UserListResource(Resource):
    @possibleException
    def get(self):
        getUserResult = Userlistresourceparser()
        return findUserById(getUserResult)
