from db_model import getLog
from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from config_reader import getDbName

class LogResource(Resource):
    def get(self, serviceName = None):
        parser_dict = parse()
        if serviceName == None:
            serviceName = getDbName()

        return getLog(serviceName, parser_dict['number'], parser_dict['offset'], 
            parser_dict['dateFrom'], parser_dict['dateTo'])
    	
