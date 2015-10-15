from db_model import getLog
from config_reader import getDbName
from flask.ext.restful import Resource
from log_parsers import LogParser
from date_utils import dateDeserialiser


NUMBER = 'number'
OFFSET = 'offset'
DATE_FROM = 'date_from'
DATE_TO = 'date_to'


class LogResource(Resource):

    def get(self, serviceName=None):
        parser_dict = LogParser.parseGetParameters()
        if serviceName is None:
            serviceName = getDbName()

        return getLog(
            serviceName,
            parser_dict[NUMBER],
            parser_dict[OFFSET],
            dateDeserialiser(
                parser_dict,
                DATE_FROM),
            dateDeserialiser(
                parser_dict,
                DATE_TO))
