from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException

class UserFindResource(Resource):
    @possibleException
    def get(self):
        pass
        #This method is empty. You can add code here
