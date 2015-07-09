from flask_restful import Resource, reqparse
from user_routines import logUserOut

KEY_USER_ID = "user_id"

class LogoutResource(Resource) :
    def get(self) :
        parser = reqparse.RequestParser();
        parser.add_argument(KEY_USER_ID, str, required = True)
        args = parser.parse_args()
        logUserOut(args[KEY_USER_ID])