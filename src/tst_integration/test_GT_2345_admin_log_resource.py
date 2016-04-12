import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = "/instance/admin/log?service_name=testservice" \
    "&number=10&subsrting=plugin"
VALID_RESPONSE_CODE = 200


class TestAdminLogResource(BasicIntegrationTest):

    def testAdminLogResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
