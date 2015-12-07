from flask_restful import Resource
from possible_exception import possibleException
from db_model import getMetadataById, setMetadata, deleteMetadataById
from metadata_resource_parser import MetadataParser

JSON = 'json'


class MetadataResource(Resource):

    @possibleException
    def get(self, serviceName, metadata_id):
        obj = getMetadataById(serviceName, metadata_id)
        return obj, 200

    @possibleException
    def put(self, serviceName, metadata_id):
        print metadata_id
        listArgs = MetadataParser.parsePutParameters()
        setMetadata(serviceName, listArgs.get(JSON), metadata_id)
        return {}, 200

    @possibleException
    def delete(self, serviceName, metadata_id):
        deleteMetadataById(serviceName, metadata_id)
        return {}, 200
