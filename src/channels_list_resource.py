from flask_restful import reqparse
from flask.ext.restful import Resource
from channels_list_parsers import ChannelsListResourceParser
from db_model import addChannel
from db_model import getChannelsList, getChannelByName
from channel_does_not_exist import ChannelDoesNotExist
from channel_already_exists import ChannelAlreadyExists

class ChannelsListResource(Resource):
    def get(self, serviceName):
        parserResult = ChannelsListResourceParser.parseGetParameters()
        return getChannelsList(serviceName, parserResult.get('substring', None), parserResult.get('number', None), parserResult.get('offset', None))

    def post(self, serviceName):
        listArgs = ChannelsListResourceParser.parsePostParameters()
        try:
        	obj = getChannelByName(serviceName, listArgs.get('name', None))
        	e = ChannelAlreadyExists()
        	return e.getReturnObject()
        except ChannelDoesNotExist as e:
        	return addChannel(listArgs.get('name', None), listArgs.get('json', None), 'STUB', serviceName)