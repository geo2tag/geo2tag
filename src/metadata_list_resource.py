from flask_restful import Resource
from possible_exception import possibleException
from db_model import setMetadata, findMetadata
from metadata_list_resource_parser import \
    MetadataListResourceParser, ARGS_QUERY, \
    ARGS_NUMBER, ARGS_OFFSET


class MetadataListResource(Resource):

    @possibleException
    def get(self, serviceName):
        args = MetadataListResourceParser.parseGetParameters()
        number = args[ARGS_NUMBER]
        offset = args[ARGS_OFFSET]
        query = args[ARGS_QUERY]
        objects = findMetadata(serviceName, number, offset,
                               query)
        return objects, 200

    @possibleException
    def post(self, serviceName):
        args = MetadataListResourceParser.parsePostParameters()
        _id = unicode(setMetadata(serviceName, args))
        return _id, 200
