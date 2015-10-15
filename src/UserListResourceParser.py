from flask.ext.restful import Resource
from possible_exception import possibleException
from flask import request


class Userlistresourceparser(Resource):

    @possibleException
    def post(self):
        number = self.request.get("name")
        