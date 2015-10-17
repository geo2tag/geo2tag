from flask.ext.restful import Resource
from possible_exception import possibleException
from user_routines import findUserById

USER_ID = 'user_id'

class UserFindResource(Resource):

    @possibleException
    def get(self):
        return findUserById(USER_ID)
