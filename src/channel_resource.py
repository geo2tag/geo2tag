from flask_restful import reqparse
from flask.ext.restful import Resource

from channel_does_not_exist import ChannelDoesNotExist
from channel_parsers import *
from db_model import updateChannel


class ChannelResource(Resource):
    
    def put(self, serviceName, channelId):
        listArgs = ChannelResourceParser.parsePutParameters()
        try:
            updateChannel(serviceName, channelId, listArgs.get(ARGS_NAME), listArgs.get(ARGS_JSON), listArgs.get(ARGS_ACL))
        except ChannelDoesNotExist as e:
    	    return e.getReturnObject()
        return {}, 200
