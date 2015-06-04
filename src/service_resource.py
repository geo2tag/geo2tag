from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from service_parsers import ServiceParser

class ServiceResource(Resource):
    def get(self, serviceName):
        return {serviceName: 'Service description'}

    def put(self, serviceName):
        parserList = ServiceParser.parsePutParameters()
        return {serviceName: 'Service updated'}

    def delete(self, serviceName):
        return {serviceName: 'Service removed'} 