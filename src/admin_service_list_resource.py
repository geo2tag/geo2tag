from flask_restful import Resource
from flask import render_template
from flask import make_response


class AdminServiceListResource(Resource):

    def get(self):
        return make_response(
            render_template(
                'service_list.html'))
