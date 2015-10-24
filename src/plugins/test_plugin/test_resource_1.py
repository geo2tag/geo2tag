from flask_restful import Resource


class TestResource1(Resource):

    def get(self):
        return 'test_resource_1'
