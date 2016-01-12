from flask import request


class MetadataParser():

    @staticmethod
    def parsePutParameters():
        return request.get_json(force=True)
