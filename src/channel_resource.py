from possible_exception import possibleException
from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import getChannelById, deleteChannelById
from channel_does_not_exist import ChannelDoesNotExist
from channel_parsers import *
from db_model import updateChannel

class ChannelResource(Resource):
    @possibleException
    def get(self, serviceName, channelId):
        obj = getChannelById(serviceName, channelId) 
        return obj, 200
    @possibleException
    def delete(self, serviceName, channelId):
        deleteChannelById(serviceName, channelId)
        return {}, 200
    @possibleException
    def put(self, serviceName, channelId):
        listArgs = ChannelResourceParser.parsePutParameters()
        updateChannel(serviceName, channelId, listArgs.get(ARGS_NAME), listArgs.get(ARGS_JSON), listArgs.get(ARGS_ACL))
        return {}, 200
