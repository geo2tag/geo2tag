from flask_restful import reqparse
from flask.ext.restful import Resource
from channels_list_parsers import ChannelsListResourceParser
from db_model import addChannel
from db_model import getChannelsList

SUBSTRING = 'substring'
NUMBER = 'number'
OFFSET = 'offset'
JSON = 'json'
STUB = 'STUB'
NAME = 'name'

class ChannelsListResource(Resource):
    def get(self, serviceName):
        parserResult = ChannelsListResourceParser.parseGetParameters()
        return getChannelsList(serviceName, parserResult.get(SUBSTRING, None), parserResult.get(NUMBER, None), parserResult.get(OFFSET, None))

    def post(self, serviceName):
        listArgs = ChannelsListResourceParser.parsePostParameters()
        return addChannel(listArgs.get(NAME, None), listArgs.get(JSON, None), STUB, serviceName)
