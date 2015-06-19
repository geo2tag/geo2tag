from flask_restful import reqparse
from flask.ext.restful import Resource
from channels_list_parsers import ChannelsListResourceParser
from channel_does_not_exist import ChannelDoesNotExist
from db_model import deleteChannelById

class ChannelsListResource(Resource):
    def get(self, serviceName):
        return ChannelsListResourceParser.parseGetParameters()

    def delete(self, serviceName):
    	try:
    		deleteChannelById(serviceName, 'channelId') 
    	except ChannelDoesNotExist as e:
    		return e.getReturnObject()
        return {}, 200

