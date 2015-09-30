import unittest
import requests
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')
from config_reader import getInstancePrefix

TEST_URL = '/' + getInstancePrefix() + '/plugin/geocoder/service/testservice/job/TEST'
VALID_RESPONSE_CODE = 404
VALID_RESPONSE_TEXT = 'Plugin is not enabled'

class TestGeocodingPluginReady(BasicIntegrationTest):
    def testGeocodingPluginReady(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
