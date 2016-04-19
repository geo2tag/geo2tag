from flask_restful import Resource
from flask import render_template, make_response
from possible_exception import possibleException
from icon_resource_parser import IconResourceParser, CHANNEL_ID
import hashlib


class IconResource(Resource):

    @possibleException
    def get(self, serviceName):
        print serviceName
        args = IconResourceParser.parseGetParameters()
        color = getColorsFromChannelId(args[CHANNEL_ID])
        return make_response(render_template('icon.svg', color=color), 200,
                             {'Content-Type': 'image/svg+xml'})


def getColorsFromChannelId(channel_id):
    hdigest = hashlib.md5(channel_id).hexdigest()
    colors = hdigest[:6]
    return colors
