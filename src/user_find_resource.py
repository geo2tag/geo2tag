from flask_restful import Resource
from possible_exception import possibleException
from user_routines import findUserById


class UserFindResource(Resource):

    @possibleException
    def get(self, user_id):
        return findUserById(user_id)
