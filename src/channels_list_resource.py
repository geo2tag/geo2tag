from flask_restful import reqparse
from flask.ext.restful import Resource
from channels_list_parsers import ChannelsListResourceParser
from db_model import addChannel

class ChannelsListResource(Resource):
    def get(self, serviceName):
        return ChannelsListResourceParser.parseGetParameters()

    def post(self, serviceName):
        listArgs = ChannelsListResourceParser.parsePostParameters()
        return addChannel(listArgs.get('name', None), listArgs.get('json', None), 'STUB', serviceName)