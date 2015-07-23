from flask_restful import reqparse
from flask.ext.restful import Resource

class ServiceListResource(Resource):
    def get(self):
    	return "Okay"