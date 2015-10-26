import requests
import json
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/plugin_config/'
VALID_RESPONSE_CODE = 200
TEST_PLUGIN_NAME = 'geocoder'
TEST_TEXT_REQ = '{"geo": {"geoname": "g"}, "main": {"host": \
"localhost", "db_name": "test", "port": "111"}, "geocoding": \
{"geonames_login": "geo2tag"}}'
TEST_TEXT_REQ1 = '{"geo": {"geoname": "g"}, "main": {"host": \
"localhost", "db_name": "test", "port": "111"}, "geocoding": \
{"geonames_login": "geo2tag"}, "section1": {"param1": "value1"}}'
DATA = {'section1': {'param1': 'value1'}}


class TestPluginConfigResource(BasicIntegrationTest):

    def test_APluginConfigResource_GET(self):
        response = requests.get(self.getUrl(TEST_URL + TEST_PLUGIN_NAME))
        responseCode = response.status_code
        responseText = response.text
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertEquals(responseText, TEST_TEXT_REQ)

    def test_PluginConfigResource_PUT(self):
        response = requests.put(self.getUrl(
            TEST_URL + TEST_PLUGIN_NAME), data=json.dumps(DATA))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL + TEST_PLUGIN_NAME))
        responseText = response.text
        self.assertEquals(responseText, TEST_TEXT_REQ1)
