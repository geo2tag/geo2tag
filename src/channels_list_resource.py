from flask_restful import reqparse
from flask.ext.restful import Resource
from channels_list_parsers import ChannelsListResourceParser
from db_model import getChannelsList
class ChannelsListResource(Resource):
    def get(self, serviceName):
        s = ChannelsListResourceParser.parseGetParameters()
        return getChannelsList(serviceName, '_', 2)
