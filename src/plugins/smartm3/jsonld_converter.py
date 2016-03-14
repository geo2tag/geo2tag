# -*- coding: utf-8 -*-
from os import path

POINT_ID = 'point_id'
LATITUDE = 'latitude'
LONGITUDE = 'longitude'
ALTITUDE = 'altitude'


def getJsonLDContext():
    CONTEXT_FILE_NAME = 'points.jsonld'
    localDir = path.dirname(__file__)    
    jsonldFullPath = path.join(localDir, CONTEXT_FILE_NAME)
    jsonldFile = open(jsonldFullPath, 'r')
    jsonldContent = jsonldFile.readlines()
    return ''.join(jsonldContent)


def converPointToJsonLD(point):
    jsonldPoint = point
    jsonldPoint[]    

    return jsonldPoint 

def convertPointsToJsonLD(points):
    return [converPointToJsonLD(x) for x in points]
