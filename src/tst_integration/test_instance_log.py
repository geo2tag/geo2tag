import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL1 = "/instance/service/testservice/log?" \
            "date_from='1983-01-22T08:00:00.000000'"
TEST_URL2 = "/instance/log?date_from='1983-01-22T08:00:00.000000'"
TEST_URL1_IV = "/instance/service/testservice/log?date_from='1111'"
TEST_URL2_IV = "/instance/log?date_from='1111'"
VALID_RESPONSE_CODE = 200
INVALID_RESPONSE_CODE = 400


class TestInstanceLogRequest(BasicIntegrationTest):

    def testInstanceLogRequest_URL1_VALID(self):
        response = requests.get(self.getUrl(TEST_URL1))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)

    def testInstanceLogRequest_URL2_VALID(self):
        response = requests.get(self.getUrl(TEST_URL2))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)

    def testInstanceLogRequest_URL1_INVALID(self):
        response = requests.get(self.getUrl(TEST_URL1_IV))
        responseCode = response.status_code
        self.assertEquals(responseCode, INVALID_RESPONSE_CODE)

    def testInstanceLogRequest_URL2_INVALID(self):
        response = requests.get(self.getUrl(TEST_URL2_IV))
        responseCode = response.status_code
        self.assertEquals(responseCode, INVALID_RESPONSE_CODE)
