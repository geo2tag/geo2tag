from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from flask import render_template
from flask import make_response


class MapResource(Resource):

    def get(self, serviceName=None):
        return make_response(render_template('map.html'))
