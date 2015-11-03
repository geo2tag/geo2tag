import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/plugin_config/'
VALID_RESPONSE_CODE = 200
TEST_PLUGIN_NAME = 'geocoder'
TEST_TEXT_REQ_1 = '{"geocoding": {"geonames_login": "geo2tag"}}'


class TestPluginConfigGeocoder(BasicIntegrationTest):

    def test_PluginConfigGecoder(self):
        response = requests.get(self.getUrl(TEST_URL + TEST_PLUGIN_NAME))
        responseCode = response.status_code
        responseText = response.text
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertEquals(responseText, TEST_TEXT_REQ_1)
