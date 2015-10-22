from flask_restful import Resource
from flask import render_template
from flask import make_response


class AdminServiceResource(Resource):

    def get(self, service_id):
        return make_response(
            render_template(
                'service.html'))
