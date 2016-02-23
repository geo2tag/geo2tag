from flask import request


class ServiceParser():

    @staticmethod
    def parsePutParameters():
        return request.get_json(force=True)
