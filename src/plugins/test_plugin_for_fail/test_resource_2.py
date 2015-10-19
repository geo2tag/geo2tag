from flask_restful import Resource


class TestResource2(Resource):

    def get(self):
        return 'test_resource_2'
