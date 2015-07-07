from flask_restful import reqparse
from flask.ext.restful import Resource
from point_list_resource_parser import PointListResourceParser
from point_parsers import PointParser
from db_model import addPoints
class PointListResource(Resource):
    def get(self, serviceName):
        newPoint = PointListResourceParser.parseGetParameters()
        return newPoint
    def post(self):
        poinList = PointParser.parsePostParameters()
        addPoints(poinList)
