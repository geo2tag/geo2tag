from flask_restful import reqparse
from flask.ext.restful import Resource
from point_list_resource_parser import PointListParser
class PointResource(Resource):
    def get(self, serviceName, pointId):
        newPoint = PointListParser.parseGetParameters()
        return newPoint
    def post(self):
        pass