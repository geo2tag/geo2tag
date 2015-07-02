from flask_restful import reqparse
from flask.ext.restful import Resource
from flask import render_template

class LoginResource(Resource):
    def get(self):
        return render_template('login.html')