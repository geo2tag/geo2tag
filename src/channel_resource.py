from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import deleteChannelById
from channel_does_not_exist import ChannelDoesNotExist
from channel_parsers import ChannelResourceParser
from db_model import updateChannel

class ChannelResource(Resource):
    def delete(self, serviceName, channelId):
        try:
            deleteChannelById(serviceName, channelId) 
        except ChannelDoesNotExist as e:
            return e.getReturnObject()
        return {}, 200

    def put(self, serviceName, channelId):
    	listArgs = ChannelResourceParser.parsePutParameters()
    	try:
    		updateChannel(serviceName, channelId, listArgs.get('name'), listArgs.get('json'), listArgs.get('acl'))
    	except ChannelDoesNotExist as e:
    		return e.getReturnObject()
    	return {}, 200