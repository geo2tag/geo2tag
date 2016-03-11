from smartm3_resource import SmartM3Resource


def getPluginResources():
    result = {'smartm3/service/<string:serviceName>/point': SmartM3Resource}
    return result


def getPluginInfo():
    inf = 'This plugin converts points data in json format to SmartM3 format'
    return inf
