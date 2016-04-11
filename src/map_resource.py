from flask_restful import Resource
from flask import render_template
from flask import make_response
from db_model import getAllChannelIds
from map_resource_parser import MapParser

NUMBER_VALUE = 1000
SERVICE_NAME = 'serviceName'
CHANNEL_IDS = 'channel_ids'
NUMBER = 'number'
LATITUDE = 'latitude'
LONGITUDE = 'longitude'


class MapResource(Resource):

    def get(self, serviceName=None):
        args = MapParser.parseGetParameters()
        for val in args.values():
            if val is not None:
                return make_response(render_template('map.html'))
        get_param = getDefaultMapParams(serviceName)
        return make_response(render_template('map.html', params=get_param))


def getDefaultMapParams(serviceName):
    result = {}
    all_channel_ids = getAllChannelIds(serviceName)
    result[CHANNEL_IDS] = all_channel_ids
    result[SERVICE_NAME] = serviceName
    result[NUMBER] = NUMBER_VALUE
    return result
