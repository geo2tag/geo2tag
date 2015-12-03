from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException

JSON = 'json'


class MetadataResource(Resource):

    @possibleException
    def get(self, serviceName, _id):
        obj = getMetadataById(service_Name, _id)
        return obj, 200

    @possibleException
    def put(self, serviceName, _id):
        listArgs = MetadataResourceParser.parsePutParameters()
        setMetadata(serviceName, listArgs.get(JSON), _id) 

    @possibleException
    def delete(self, serviceName, _id):
        deleteMetadataById(service_Name, _id)
        return {}, 200
