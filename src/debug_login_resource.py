from flask_restful import reqparse
from flask.ext.restful import Resource
from config_reader import getDebugUsers;


    def parseId():
        parser = reqparse.RequestParser()
        parser.add_argument(_id, type=string, default=None)
        args = parser.parse_args()
        return args


class DebugLoginResource(Resource):
    def get(self, _id):
        parser_dict = parseId()
        usersList = getDebugUsers
        _id = parser_dict[_id]
        if  _id in usersList:
        	logUserIn(_id)
        else:
        	#return ('Credentials are incorrect', 401)




        return getLog(serviceName, parser_dict[NUMBER], parser_dict[OFFSET], 
            dateDeserialiser(parser_dict, DATE_FROM), dateDeserialiser(parser_dict, DATE_TO))