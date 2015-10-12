import flask_restful as restful
from flask_restful import Resource


class StatusResource(Resource):

    def get(self):
        return 'OK'
