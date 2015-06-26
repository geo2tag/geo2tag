from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import getChannelById, deleteChannelById
from channel_does_not_exist import ChannelDoesNotExist
from channel_parsers import *
from db_model import updateChannel

class ChannelResource(Resource):
    def get(self, serviceName, channelId):
        try:
            obj = getChannelById(serviceName, channelId) 
        except ChannelDoesNotExist as e:
            return e.getReturnObject()
        return obj, 200

    def delete(self, serviceName, channelId):
        try:
            deleteChannelById(serviceName, channelId) 
        except ChannelDoesNotExist as e:
            return e.getReturnObject()
        return {}, 200

    def put(self, serviceName, channelId):
        listArgs = ChannelResourceParser.parsePutParameters()
        try:
            updateChannel(serviceName, channelId, listArgs.get(ARGS_NAME), listArgs.get(ARGS_JSON), listArgs.get(ARGS_ACL))
        except ChannelDoesNotExist as e:
    	    return e.getReturnObject()
        return {}, 200
