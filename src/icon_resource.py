from flask_restful import Resource
from possible_exception import possibleException
from icon_resource_parser import IconResourceParser, MARKER, RADIUS, CHANNEL_ID
import hashlib
import json


class IconResource(Resource):

    @possibleException
    def get(self, serviceName):
        print serviceName
        args = IconResourceParser.parseGetParameters()
        template = generateMarkerSvgCode(
            json.loads(args[MARKER]), args[RADIUS], args[CHANNEL_ID])
        return render_template("icon.svg", template = template)


def generateMarkerSvgCode(marker, radius, channel_id):
    template = u'<svg><circle cx="X_PH" cy="Y_PH" r="RADIUS_PH" ' + \
        'transform="matrix(1 0 0 1 0 0)" ' + \
        'style="fill: rgb("R_PH", "G_PH", "B_PH"); ' + \
        'cursor: move;"></circle></svg>'
    colors = getColorsFromChannelId(channel_id)
    placeHolders = {'X_PH': u'x', 'Y_PH': u'y', 'R_PH': 'R',
                    'G_PH': 'G', 'B_PH': 'B'}
    marker.update(colors)
    for placeHolder in placeHolders:
        field = placeHolders[placeHolder]
        template = template.replace(placeHolder, marker[field])
    template = template.replace('RADIUS_PH', str(radius))
    return template


def getColorsFromChannelId(channel_id):
    hdigest = hashlib.md5(channel_id).hexdigest()
    colors = {"R": hdigest[:2], "G": hdigest[3:5], "B": hdigest[6:8]}
    return colors
