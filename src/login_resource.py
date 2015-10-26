# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import render_template, make_response
from user_routines import getUser


class LoginResource(Resource):

    def get(self):
        user = getUser()
        return make_response(
            render_template(
                'login.html',
                user=user,
                instance_prefix='instance'))
