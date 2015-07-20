from flask_restful import reqparse
from flask.ext.restful import Resource
from point_list_resource_parser import PointListResourceParser, \
    CHANNEL_IDS, NUMBER, GEOMETRY, ALTITUDE_FROM, ALTITUDE_TO,  \
    SUBSTRING, DATE_FROM, DATE_TO, OFFSET, RADIUS 

from db_model import addPoints, findPoints

class PointListResource(Resource):
    def get(self, serviceName):
        params = PointListResourceParser.parseGetParameters()
        result = findPoints ( serviceName, params[CHANNEL_IDS], \
            params[NUMBER], params[GEOMETRY], params[ALTITUDE_FROM], \
            params[ALTITUDE_TO], params[SUBSTRING], params[DATE_FROM], \
            params[DATE_TO], params[OFFSET], params[RADIUS])        

        return result

    def post(self, serviceName):
        try:
            poinList = PointListResourceParser.parsePostParameters()
        except ValueError as e:
            return {}, 400
        addPoints(serviceName, poinList)
        return {}, 200
