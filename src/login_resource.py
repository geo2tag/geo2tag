# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import render_template, make_response, session


class LoginResource(Resource):

    def get(self):
        print "____________________User"
        
        if 'user_login' in session:
            user = session['user_login']
        elif 'user_id' in session:
            user = session['user_id']
        else:
            user = 'Anonym'
        print user
        return make_response(
            render_template(
                'login.html',
                user = user,
                instance_prefix='instance'))
