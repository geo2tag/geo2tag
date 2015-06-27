from flask_restful import reqparse
from flask.ext.restful import Resource
from point_does_not_exist import PointDoesNotExist
from point_resource_parsers import PointResourceParsers
from db_model import updatePoint
class PointResource(Resource):
    def get(self, serviceName, pointId):
        pass
    def post(self):
        pass
    def put(self, serviceName, pointId):
        args = PointResourceParsers.parsePutParameters()
        try:
            updatePoint(serviceName, pointId, args)
        except PointDoesNotExist as e:
            return e.getReturnObject()
        return {}, 200
    def delete(self):
        pass