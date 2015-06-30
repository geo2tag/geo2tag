from flask_restful import reqparse
from flask.ext.restful import Resource
from point_does_not_exist import PointDoesNotExist
from db_model import getPointById
class PointResource(Resource):
    def get(self, serviceName, pointId):
        try:
            newPoint = getPointById(serviceName, pointId)
        except PointDoesNotExist as e:
            return e.getReturnObject()
        return newPoint
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
