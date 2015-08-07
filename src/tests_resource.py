from flask.ext.restful import Resource
from flask import render_template
from flask import make_response
from config_reader import getInstancePrefix


class TestsResource(Resource):

    def get(self):
<<<<<<< HEAD
        return make_response(render_template('tests.html'))
=======
        return make_response(
            render_template(
                'tests.html',
                instancePrefix=getInstancePrefix()))
>>>>>>> dd7065fe407c8a2960f83a15821eb88ef1d4e847
