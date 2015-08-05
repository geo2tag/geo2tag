import unittest
import requests, json
from flask import Flask, request
from basic_integration_test import BasicIntegrationTest



TEST_URL_NO_DATA = '/instance/service/testservice/map'
TEST_URL_DATA = '/instance/service/testservice/map?number=100&channel_ids=556721a52a2e7febd2744202&channel_ids=556721a52a2e7febd2744201&date_from=1000-01-01T01:01:01'
VALID_RESPONSE_CODE = 200
class TestRoutMap(BasicIntegrationTest):
    def testRoutMapRequestNoData(self):
        response = requests.get(self.getUrl(TEST_URL_NO_DATA))
        responseCode = response.status_code
        responseText = response.text
        self.assertEqual(VALID_RESPONSE_CODE,responseCode)
        
    def testRoutMapRequestData(self):
        response = requests.get(self.getUrl(TEST_URL_DATA))
        responseCode = response.status_code
        responseText = response.text
        self.assertEqual(VALID_RESPONSE_CODE,responseCode)
