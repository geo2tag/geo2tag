from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from flask import render_template
from flask import make_response
from base_geo2tag_exception import BaseGeo2TagException
from point_list_resource_parser import PointListResourceParser
from db_model import getAllChannelIds

NUMBER_VALUE = 1000
SERVICE_NAME = 'serviceName'
CHANNEL_IDS = 'channel_ids'
NUMBER = 'number'


class MapResource(Resource):

    def get(self, serviceName=None):
        try:
            args = PointListResourceParser.parseGetParameters()
            args[SERVICE_NAME] = serviceName
            get_param = args
            return make_response(render_template('map.html', params=get_param))
        except Exception as e:
            get_param = getDefaultMapParams(serviceName)
            return make_response(render_template('map.html', params=get_param))


def getDefaultMapParams(serviceName):
    result = {}
    all_channel_ids = getAllChannelIds(serviceName)
    result[CHANNEL_IDS] = all_channel_ids
    result[SERVICE_NAME] = serviceName
    result[NUMBER] = NUMBER_VALUE
    return result
