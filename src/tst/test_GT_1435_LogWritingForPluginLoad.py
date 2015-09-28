from unittest import TestCase
import pymongo
import os
from bson import objectid
from flask import Flask
from flask.ext.restful import Api
from plugin_routines import enablePlugin
from db_model import getDbName, getDbObject
from log import writeInstanceLog

tstDir = os.getcwd()
srcDir = tstDir + '/..'

app = Flask(__name__)
api = Api(app)

db = getDbObject(getDbName())

PLUGIN_DONE_PLUGIN = 'test_plugin'
PLUGIN_FAIL_PLUGIN = 'test_plugin_for_load_fail_gt_1435'
FIELD_USERID = 'user_id'
COLLECTION_LOG = 'log'
FIELD_MESSAGE = 'message'
ID = '_id'
ANONYM_USER = 'anonym'

MESSAGE_LOAD_DONE = 'Plugin ' + PLUGIN_DONE_PLUGIN + ' successfully loaded'
MESSAGE_LOAD_FAIL = 'Error occurred while loading the plugin ' + PLUGIN_FAIL_PLUGIN


class TestLogWritingForPluginLoad(TestCase):

    def setUp(self):
        os.chdir(srcDir)

    def tearDown(self):
        os.chdir(tstDir)

    def testLogWritingForPluginLoadDone(self):
        enablePlugin(api, PLUGIN_DONE_PLUGIN)
        last_log_document = db[COLLECTION_LOG].find().sort(
            ID, pymongo.DESCENDING).limit(1)
        self.assertNotEqual(
            last_log_document[0][FIELD_MESSAGE].find(MESSAGE_LOAD_DONE), -1)
        self.assertEqual(last_log_document[0][FIELD_USERID], ANONYM_USER)

    def testLogWritingForPluginLoadFail(self):
        enablePlugin(api, PLUGIN_FAIL_PLUGIN)
        last_log_document = db[COLLECTION_LOG].find().sort(
            ID, pymongo.DESCENDING).limit(1)
        self.assertNotEqual(
            last_log_document[0][FIELD_MESSAGE].find(MESSAGE_LOAD_FAIL), -1)
        self.assertEqual(last_log_document[0][FIELD_USERID], ANONYM_USER)
