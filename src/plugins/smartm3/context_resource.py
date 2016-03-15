from flask_restful import Resource 
from jsonld_converter import getJsonLDContext 


class ContextResource(Resource):

    def get(self):
        return getJsonLDContext()
