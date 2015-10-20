from flask.ext.restful import Resource
from possible_exception import possibleException
from user_routines import findUserById
from flask import make_response


USER_ID = '_id'


class UserFindResource(Resource):

    @possibleException
    def get(self, user_id=None):
        return findUserById(user_id)
