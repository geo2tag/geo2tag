import flask_restful as restful
from flask_restful import Resource
from flask import render_template
from flask import make_response
from config_reader import getInstancePrefix


class InternalTestsResource(Resource):

    def get(self):
        return make_response(
            render_template(
                'internal_tests.html',
                instancePrefix=getInstancePrefix()))
