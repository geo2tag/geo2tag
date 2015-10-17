import unittest
import os
from flask import Flask
import flask_restful as restful
from flask_restful import Api
from plugin_routines import enablePlugin


class TestGt1416(unittest.TestCase):

    def testGt1416(self):
        app = Flask(__name__)
        api = Api(app)
        os.chdir('../')
        enablePlugin(api, 'testPlugin1')
        os.chdir('tst')
        self.assertTrue('resource_gt_1416' in api.endpoints)
