# -*- coding: utf-8 -*-
from os import path
from date_utils import dateSerialiser

# Keys to be renamed
ALT = 'alt'
LOCATION = 'location'
COORDINATES = 'coordinates'
ID = '_id'

# New keys
POINT_ID = 'point_id'
LATITUDE = 'latitude'
LONGITUDE = 'longitude'
ALTITUDE = 'altitude'

# Changed keys
CHANNEL_ID = 'channel_id'
DATE = 'date'

# Unchanged keys
BC = 'bc'
JSON = 'json'
UNCHANGED_KEYS = [BC, JSON]

CONTEXT = '@context'
CONTEXT_PATH = '/instance/plugins/smartm3/point.jsonld'


def getJsonLDContext():
    CONTEXT_FILE_NAME = 'points.jsonld'
    localDir = path.dirname(__file__)
    jsonldFullPath = path.join(localDir, CONTEXT_FILE_NAME)
    jsonldFile = open(jsonldFullPath, 'r')
    jsonldContent = jsonldFile.readlines()
    return ''.join(jsonldContent)


def convertPointToJsonLD(point):
    jsonldPoint = {}
    # Copying unchanged keys
    for key in UNCHANGED_KEYS:
        jsonldPoint[key] = point[key]

    # Changing format of existing keys
    jsonldPoint[CHANNEL_ID] = unicode(point[CHANNEL_ID])
    jsonldPoint[DATE] = dateSerialiser(point[DATE])

    # Renaming existing keys
    jsonldPoint[POINT_ID] = unicode(point[ID])
    jsonldPoint[ALTITUDE] = point[ALT]
    coordinates = point[LOCATION][COORDINATES]
    jsonldPoint[LONGITUDE] = coordinates[0]
    jsonldPoint[LATITUDE] = coordinates[1]

    jsonldPoint[CONTEXT] = CONTEXT_PATH

    return jsonldPoint


def convertPointsToJsonLD(points):
    return [convertPointToJsonLD(x) for x in points]
