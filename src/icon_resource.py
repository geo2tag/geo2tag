from flask_restful import Resource
from possible_exception import possibleException
from icon_resource_parser import IconResourceParser, CHANNEL_ID
import hashlib


class IconResource(Resource):

    @possibleException
    def get(self, serviceName):
        print serviceName
        args = IconResourceParser.parseGetParameters()
        template = generateMarkerSvgCode(args[CHANNEL_ID])
        return render_template("icon.svg", template = template)


def generateMarkerSvgCode(channel_id):
    template = u'<svg><circle cx="5" cy="5" r="10" ' + \
        'transform="matrix(1 0 0 1 0 0)" ' + \
        'fill="#PH_COLOR"' + \
        'cursor: move;"></circle></svg>'
    colors = getColorsFromChannelId(channel_id)
    template = template.replace('PH_COLOR', colors)
    return template


def getColorsFromChannelId(channel_id):
    hdigest = hashlib.md5(channel_id).hexdigest()
    colors = hdigest[:6]
    return colors
