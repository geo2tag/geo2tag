from flask.ext.restful import Resource
from flask import render_template
from flask import make_response
from config_reader import getInstancePrefix
class TestsResource(Resource):
    def get(self):
        return make_response(render_template('tests.html', instancePrefix=getInstancePrefix()))
