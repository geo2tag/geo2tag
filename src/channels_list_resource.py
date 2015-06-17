from flask_restful import reqparse
from flask.ext.restful import Resource
from channels_list_parsers import ChannelsListResourceParser

class ChannelsListResource(Resource):
    def get():
        return ChannelsListResource.parseGetParameters()

