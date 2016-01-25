from flask_restful import Resource
from flask import render_template
from flask import make_response


class AdminPluginConfigResource(Resource):

    def get(self, pluginName):
        print pluginName
        return make_response(
            render_template(
                'plugin_config.html'))
