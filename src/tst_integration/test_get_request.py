import requests
from basic_integration_test import BasicIntegrationTest
from db_model import removeService, getDbObject

TEST_URL = '/instance/service'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '[]'
NOT_VALID_RESPONSE_CODE = 400
BAD_RESULT = '{"message": "[offset]: invalid literal for int() ' \
             'with base 10: \'string\'"}'

TEST_NAME = 'name_service_test_get'
TEST_OBJ = {"name": TEST_NAME, "offset": 12}
TEST_PARAMETERS = {"offset": 12}
BAD_TEST_PARAMETERS = {"offset": "string"}

COLLECTION = 'services'


class TestServiceListGetRequest(BasicIntegrationTest):

    def testServiceListGetRequest(self):
        db = getDbObject()
        db[COLLECTION].save(TEST_OBJ)
        response = requests.get(self.getUrl(TEST_URL),
                                params=TEST_PARAMETERS)
        removeService(TEST_NAME)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(
            self.getUrl(TEST_URL),
            params=BAD_TEST_PARAMETERS)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, BAD_RESULT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
