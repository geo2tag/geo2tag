from flask_restful import Resource
from flask import render_template
from flask import make_response


class AdminPluginListResource(Resource):

    def get(self):
        return make_response(
            render_template(
                'plugin_config.html'))
