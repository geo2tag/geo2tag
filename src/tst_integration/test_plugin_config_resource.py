import requests
import json
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/plugin_config/'
VALID_RESPONSE_CODE = 200
TEST_PLUGIN_NAME = 'geocoder'
TEST_PLUGIN_NAME1 = '"geocoder"'
DATA = {'section1': {'param1': 'value1'}}


class TestPluginConfigResource(BasicIntegrationTest):

    def testPluginConfigResource_GET(self):
        response = requests.get(self.getUrl(TEST_URL + TEST_PLUGIN_NAME))
        responseCode = response.status_code
        responseText = response.text
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertEquals(responseText, TEST_PLUGIN_NAME1)

    def testPluginConfigResource_PUT(self):
        response = requests.put(self.getUrl(
            TEST_URL + TEST_PLUGIN_NAME), data=json.dumps(DATA))
        responseCode = response.status_code
        responseText = response.text
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertEquals(responseText, json.dumps(DATA))
