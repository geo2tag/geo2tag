from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import deletePointById, getPointById
from point_does_not_exist import PointDoesNotExist

class PointResource(Resource):
    def delete(self, serviceName, pointId):
        try:
            deletePointById(serviceName, pointId) 
        except PointDoesNotExist as e:
            return e.getReturnObject()
        return {}, 200

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