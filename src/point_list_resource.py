from flask_restful import reqparse
from flask.ext.restful import Resource
from point_list_resource_parser import PointListResourceParser, \
    CHANNEL_IDS, NUMBER, GEOMETRY, ALTITUDE_FROM, ALTITUDE_TO,  \
    SUBSTRING, DATE_FROM, DATE_TO, OFFSET, RADIUS
from possible_exception import possibleException
from db_model import addPoints, findPoints
from bson.json_util import dumps
from date_utils import dateDeserialiser


class PointListResource(Resource):

    @possibleException
    def get(self, serviceName):
        params = PointListResourceParser.parseGetParameters()
        result = findPoints(
            serviceName,
            params[CHANNEL_IDS],
            params[NUMBER],
            params[GEOMETRY],
            params[ALTITUDE_FROM],
            params[ALTITUDE_TO],
            params[SUBSTRING],
            dateDeserialiser(
                params,
                DATE_FROM),
            dateDeserialiser(
                params,
                DATE_TO),
            params[OFFSET],
            params[RADIUS])
        return result

    @possibleException
    def post(self, serviceName):
        try:
            poinList = PointListResourceParser.parsePostParameters()
        except ValueError as e:
            return {}, 400
        result = addPoints(serviceName, poinList)
        return result
