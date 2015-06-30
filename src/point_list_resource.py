from flask_restful import reqparse
from flask.ext.restful import Resource
from point_list_resource_parser import PointListResourceParser
class PointListResource(Resource):
    def get(self, serviceName):
        newPoint = PointListResourceParser.parseGetParameters()
        return newPoint
    def post(self):
        pass