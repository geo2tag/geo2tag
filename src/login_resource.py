# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import render_template, make_response


class LoginResource(Resource):

    def get(self):
        return make_response(
            render_template(
                'login.html',
                instance_prefix='instance'))
