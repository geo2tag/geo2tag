from flask.ext.restful import Resource

class test_plugin_for_done_GT_1435(Resource):
    def get(self):
        return 'test_plugin_for_done_GT_1435'

def getPluginResources():
    return {'test_plugin_for_done_GT_1435':test_plugin_for_done_GT_1435}
