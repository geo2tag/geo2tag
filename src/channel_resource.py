from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import deleteChannelById
from channel_does_not_exist import ChannelDoesNotExist
class ChannelResource(Resource):
    def delete(self, serviceName, channelId):
        try:
            deleteChannelById(serviceName, channelId) 
        except ChannelDoesNotExist as e:
            return e.getReturnObject()
        return {}, 200
