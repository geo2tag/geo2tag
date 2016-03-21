import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/' + \
    'testservice/metadata'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400
VALID_POST_ARGS = '{"json": {"name": "test_metadata_put"}}'
NOT_VALID_POST_ARGS = "not_valid_data"
VALID_GET_ARGS1 = '?number=1&offset=0&query={"a":1}'
NOT_VALID_GET_ARGS = '?arg=1'
VALID_GET_ARGS2 = '?number=1&offset=0'


class TestMetadataListResource(BasicIntegrationTest):

    def testMetadataListResourceGet(self):
        response = requests.get(self.getUrl(TEST_URL) + VALID_GET_ARGS1)
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL) + VALID_GET_ARGS2)
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL) + NOT_VALID_GET_ARGS)
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)

    def testMetadataListResourcePost(self):
        response = requests.post(self.getUrl(TEST_URL), data=VALID_POST_ARGS)
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.post(
            self.getUrl(TEST_URL),
            data=NOT_VALID_POST_ARGS)
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
