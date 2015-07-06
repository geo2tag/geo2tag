from flask_restful import Resource, reqparse
from flask import session
from bson import ObjectId

from main import app

class LogoutResource(Resource) :
    def get(self) :
        parser = reqparse.RequestParser();
        parser.add_argument("user_id", str, default=None)
        args = parser.parse_args()
        
        if args["user_id"] in session :
            session.pop(args["user_id"], None)

        #Setting random secret key
        from os import urandom
        app.secret_key = urandom(32)