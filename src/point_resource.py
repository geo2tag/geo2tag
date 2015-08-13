from possible_exception import possibleException
from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import deletePointById, getPointById, updatePoint
from point_does_not_exist import PointDoesNotExist
from point_resource_parsers import PointResourceParsers


class PointResource(Resource):

    @possibleException
    def get(self, serviceName, pointId):
        newPoint = getPointById(serviceName, pointId)
        return newPoint

    @possibleException
    def put(self, serviceName, pointId):
        args = PointResourceParsers.parsePutParameters()
        updatePoint(serviceName, pointId, args)
        return {}, 200

    @possibleException
    def delete(self, serviceName, pointId):
        deletePointById(serviceName, pointId)
        return {}, 200
