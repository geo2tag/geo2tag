import unittest
import requests
from basic_integration_test import BasicIntegrationTest
import sys
import json

TEST_URL = '/instance/plugin'
PLUGIN_NAME = 'geocoder'
PLUGIN_ENABLED = True


class TestGeocodingPluginReady(BasicIntegrationTest):

    def testGeocodingPluginReady(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        responseText = json.loads(responseText)
        self.assertEqual(responseText[PLUGIN_NAME], PLUGIN_ENABLED)
