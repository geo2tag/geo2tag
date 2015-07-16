from flask_restful import Resource
from user_routines import logUserOut

class LogoutResource(Resource) :
    def get(self) :
        logUserOut()