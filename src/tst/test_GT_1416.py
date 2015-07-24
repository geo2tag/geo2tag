import unittest
import sys
import os
from flask import Flask
from flask.ext.restful import Api
sys.path.append('../')
from plugins import enablePlugin

class TestGt1416(unittest.TestCase):
    def testGt1416(self):
        app = Flask(__name__)
        api = Api(app)
        os.chdir('../')
        enablePlugin(api, 'testPlugin1')
        self.assertTrue('resource_gt_1416' in api.endpoints)