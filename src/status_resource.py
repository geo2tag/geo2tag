from flask.ext.restful import Resource


class StatusResource(Resource):

    def get(self):
        return 'OK'
