import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/testservice/metadata/552833515404411781370711'
VALID_RESPONSE_CODE = 200


class TestMetadataResource(BasicIntegrationTest):

    def testMetadataResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
