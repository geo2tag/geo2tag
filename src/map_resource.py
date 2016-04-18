import hashlib
from flask_restful import Resource
from flask import render_template
from flask import make_response
from db_model import getAllChannelIds
from map_resource_parser import MapParser

CHANNEL_IDS = 'channel_ids'


class MapResource(Resource):

    def get(self, serviceName=None):
        args = MapParser.parseGetParameters()
        result = {CHANNEL_IDS: []}
        if args[CHANNEL_IDS] is None:
            result.update(getDefaultChannelIds(serviceName))
        print result
        return make_response(
            render_template(
                'map.html',
                params=result))


def getDefaultChannelIds(serviceName):
    result = {}
    all_channel_ids = getAllChannelIds(serviceName)
    result[CHANNEL_IDS] = all_channel_ids
    return result


def generateMarkerSvgCode(marker, radius, channel_id):
    template = u'<svg><circle cx="X_PH" cy="Y_PH" r="RADIUS_PH" ' + \
        'transform="matrix(1 0 0 1 0 0)" ' + \
        'style="fill: rgb("R_PH", "G_PH", "B_PH"); ' + \
        'cursor: move;"></circle></svg>'
    colors = getColorsFromChannelId(channel_id)
    placeHolders = {'X_PH': 'x', 'Y_PH': 'y', 'R_PH': 'R',
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
