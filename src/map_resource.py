from flask_restful import Resource
from flask import render_template
from flask import make_response
from point_list_resource_parser import PointListResourceParser
from db_model import getAllChannelIds

NUMBER_VALUE = 1000
SERVICE_NAME = 'serviceName'
CHANNEL_IDS = 'channel_ids'
NUMBER = 'number'
LATITUDE = 'latitude'
LONGITUDE = 'longitude'


class MapResource(Resource):

    def get(self, serviceName=None):
        try:
            args = PointListResourceParser.parseGetParameters()
            args[SERVICE_NAME] = serviceName
            get_param = args
            return make_response(render_template('map.html', params=get_param))
        except Exception:
            get_param = getDefaultMapParams(serviceName)
            return make_response(render_template('map.html', params=get_param))


def getDefaultMapParams(serviceName):
    result = {}
    all_channel_ids = getAllChannelIds(serviceName)
    result[CHANNEL_IDS] = all_channel_ids
    result[SERVICE_NAME] = serviceName
    result[NUMBER] = NUMBER_VALUE
    return result
