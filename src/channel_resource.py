from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import getChannelById
from channel_does_not_exist import ChannelDoesNotExist

class ChannelResource(Resource):
    def get(self, serviceName, channelId):
        try:
            obj = getChannelById(serviceName, channelId) 
        except ChannelDoesNotExist as e:
            return e.getReturnObject()
        return obj, 200