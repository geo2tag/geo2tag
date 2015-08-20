from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from flask import render_template
from flask import make_response
from base_exception import BaseException
from point_list_resource_parser import PointListResourceParser


class MapResource(Resource):

    def get(self, serviceName=None):
        try:
            args = PointListResourceParser.parseGetParameters()
            args['serviceName'] = serviceName
            getparam = args
            return make_response(render_template('map.html', params=getparam))
        except Exception as e:
            return make_response(render_template('map.html'))