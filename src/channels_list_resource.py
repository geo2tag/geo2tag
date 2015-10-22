from possible_exception import possibleException
from flask_restful import Resource
from channels_list_parsers import ChannelsListResourceParser
from db_model import addChannel
from db_model import getChannelsList, getChannelByName
from channel_does_not_exist import ChannelDoesNotExist

SUBSTRING = 'substring'
NUMBER = 'number'
OFFSET = 'offset'
JSON = 'json'
STUB = 'STUB'
NAME = 'name'


class ChannelsListResource(Resource):

    @possibleException
    def get(self, serviceName):
        parserResult = ChannelsListResourceParser.parseGetParameters()
        return getChannelsList(
            serviceName, parserResult.get(
                SUBSTRING, None), parserResult.get(
                NUMBER, None), parserResult.get(
                OFFSET, None))

    @possibleException
    def post(self, serviceName):
        listArgs = ChannelsListResourceParser.parsePostParameters()
        try:
            getChannelByName(serviceName, listArgs.get(NAME, None))
        except ChannelDoesNotExist:
            return addChannel(
                listArgs.get(
                    NAME, None), listArgs.get(
                    JSON, None), STUB, serviceName)
