from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from flask import render_template
from flask import make_response
from base_exception import BaseException
from point_list_resource_parser import PointListResourceParser
from db_model import getAllChannelIds

NUMBER = 1000
SERVICE_NAME = 'serviceName'
CHANNEL_IDS = 'channel_ids'


class MapResource(Resource):

    def get(self, serviceName=None):
        try:
            args = PointListResourceParser.parseGetParameters()
            args[SERVICE_NAME] = serviceName
            get_param = args
            return make_response(render_template('map.html', params=get_param))
        except Exception as e:
            get_param = getDefaultMapParams(serviceName, NUMBER)
            return make_response(render_template('map.html', params=get_param))


def getDefaultMapParams(serviceName, number):
    result = {}
    all_channel_ids = getAllChannelIds(serviceName)
    for i in range(number, len(all_channel_ids)):
        all_channel_ids.pop()
    result[CHANNEL_IDS] = all_channel_ids
    result[SERVICE_NAME] = serviceName
    return result
