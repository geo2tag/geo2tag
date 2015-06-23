from flask_restful import reqparse
from flask.ext.restful import Resource
from channels_list_parsers import ChannelsListResourceParser
from db_model import addChannel
from db_model import getChannelsList

class ChannelsListResource(Resource):
    def get(self, serviceName):
        parserResult = ChannelsListResourceParser.parseGetParameters()
        return getChannelsList(serviceName, parserResult.get('substring', None), parserResult.get('number', None), parserResult.get('offset', None))

    def post(self, serviceName):
        listArgs = ChannelsListResourceParser.parsePostParameters()
        return addChannel(listArgs.get('name', None), listArgs.get('json', None), 'STUB', serviceName)