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
            getparam = args
            return make_response(render_template('map.html', params=getparam))
        except Exception as e:
            getparam = getDefaultMapParams(serviceName, NUMBER)
            return make_response(render_template('map.html', params=getparam))


def getDefaultMapParams(serviceName, number):
    res = {}
    allchannelid = getAllChannelIds(serviceName)
    res[CHANNEL_IDS] = allchannelid
    res[SERVICE_NAME] = serviceName
    return res
