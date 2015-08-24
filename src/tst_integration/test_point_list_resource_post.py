import unittest
import requests
import json
from pymongo import MongoClient
from flask import Flask, request
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')
from db_model import addPoints, getDbObject
from bson.objectid import ObjectId

DB = "testservice"
COLLECTION = 'points'
JSON = 'json'
LAT = 'lat'
LON = 'lon'
CHANNEL_ID = 'channel_id'
ALT = 'alt'
CHANNEL_IDS_VALUE = 'channel_id_value'
TEST_URL = '/instance/service/testservice/point'
BAD_TEST_URL = '/instance/service/testservice/point'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400


class TestPointListPostRequest(BasicIntegrationTest):

    def testPointListPostRequest(self):
        db = getDbObject(DB)
        response = requests.post(self.getUrl(TEST_URL), data=json.dumps(
            [{LAT: 1.1, LON: 1.1, ALT: 1.1, JSON: {'a': 'b'}, CHANNEL_ID: 'channel_id_value'}]))
        responseCode = response.status_code
        responseText = response.text
        obj1 = db[COLLECTION].find_one({CHANNEL_ID: CHANNEL_IDS_VALUE})
        self.assertEquals([str(obj1['_id'])], eval(responseText))
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.post(self.getUrl(TEST_URL), data=json.dumps(
            [{LAT: '1.1', LON: 1.1, ALT: 1.1, JSON: [], CHANNEL_ID:''}]))
        responseCode = response.status_code
        responseText = response.text
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
        self.assertEquals(responseText, '{}')
