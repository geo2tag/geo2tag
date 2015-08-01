from flask_restful import reqparse

def pluginsDictRequest(plugins):
    pluginsList = plugins.split('&')
    pluginDict = {}
    for plugin in pluginsList:
        somePlugin = plugin.split('=')
        if somePlugin[1].lower() == 'true':
            somePlugin[1] = True
        elif somePlugin[1].lower() == 'false':
            somePlugin[1] = False
        else:
            continue
        pluginDict[somePlugin[0]] = somePlugin[1]
    return pluginDict

class ManagePluginsParser():
    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(NUMBER, type=pluginsDictRequest)
