import unittest
from flask import Flask
from flask_restful import Api
from rest_api_routines import initApp


class TestGt1417(unittest.TestCase):

    def testGt1417(self):
        app = Flask(__name__)
        api = Api(app)
        initApp(api)
        resources = api.endpoints
        self.assertTrue('resource_gt_1416' in resources)
        self.assertTrue('resource_gt_1417' in resources)
