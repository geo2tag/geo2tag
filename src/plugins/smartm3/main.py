from smartm3_resource import SmartM3Resource
from context_resource import ContextResource


def getPluginResources():
    result = {'service/<string:serviceName>/point': SmartM3Resource,
              'point.jsonld': ContextResource}
    return result


def getPluginInfo():
    inf = 'This plugin converts points data in json format to SmartM3 format'
    return inf
