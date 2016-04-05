from flask_restful import Resource
from flask import render_template
from flask import make_response
from admin_log_parser import LogAdminParser
from db_model import getLog

SUBSTRING = 'substring'
NUMBER = 'number'
OFFSET = 'offset'


class AdminLogResource(Resource):

    def get(self):
        parser_dict = AdminLogParser.parseGetParameters()
        number = parser_dict[NUMBER]
        offset = parser_dict[OFFSET]
        substr = parser_dict[SUBSTRING]
        getLog()
        return make_response(
            render_template(
                'log.html'))
