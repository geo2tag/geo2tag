from flask_restful import Resource
from point_list_resource_parser import PointListResourceParser, \
    CHANNEL_IDS, NUMBER, GEOMETRY, ALTITUDE_FROM, ALTITUDE_TO,  \
    SUBSTRING, DATE_FROM, DATE_TO, OFFSET, RADIUS
from db_model import findPoints
from date_utils import dateDeserialiser

# Custom error for BC dates flags
BC_DATES_FLAGS_ERR_VAL = ': Missing required parameter in the JSON body ' \
                         'or the post body or the query string'
BC_DATES_FLAGS_ERR_KEY = 'message'
POINT_LIST_PARSER_ERRS_KEY = 'err'


class SmartM3Resource(Resource):

    def get(self, serviceName):
        params_with_errs = PointListResourceParser.parseGetParameters()

        # Generating error string for 'bc_from' and 'bc_to' parameters if error
        # appeared
        if len(params_with_errs[POINT_LIST_PARSER_ERRS_KEY]) > 0:
            err_str = ""
            for i in params_with_errs[POINT_LIST_PARSER_ERRS_KEY]:
                err_str += '[' + i + '] '
            # GET request will return 'standard' error for bad parameters
            return {BC_DATES_FLAGS_ERR_KEY: err_str +
                    BC_DATES_FLAGS_ERR_VAL}, 400

        params = params_with_errs
        result = findPoints(
            serviceName,
            params[CHANNEL_IDS],
            params[NUMBER],
            params[GEOMETRY],
            params[ALTITUDE_FROM],
            params[ALTITUDE_TO],
            params[SUBSTRING],
            dateDeserialiser(
                params,
                DATE_FROM),
            dateDeserialiser(
                params,
                DATE_TO),
            params[OFFSET],
            params[RADIUS])
        # convert points to json-ld
        return result

