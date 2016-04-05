from flask_restful import Resource
from flask import render_template
from flask import make_response
from admin_log_parser import AdminLogParser
from db_model import getLog
from date_utils import dateDeserialiser

SUBSTRING = 'substring'
NUMBER = 'number'
OFFSET = 'offset'
SERVICE = 'service_name'
DATE_FROM = 'date_from'
DATE_TO = 'date_to'


class AdminLogResource(Resource):

    def get(self):
        parser_dict = AdminLogParser.parseGetParameters()
        getLog(parser_dict[SERVICE],
               parser_dict[NUMBER],
               parser_dict[OFFSET],
               dateDeserialiser(
            parser_dict,
            DATE_FROM),
            dateDeserialiser(
            parser_dict,
            DATE_TO),
            parser_dict[SUBSTRING])
        return make_response(
            render_template(
                'log.html'))
