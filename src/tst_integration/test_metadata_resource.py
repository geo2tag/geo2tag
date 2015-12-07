import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/testservice/metadata/552833515404411781370711'
VALID_RESPONSE_CODE = 200
NOT_VALID_URL = '/instance/service/testservice/metadata/552833515404411781370710'
NOT_VALID_RESPONSE_CODE = 400
NOT_VALID_RESPONSE_CODE_GET = 404
LIST_ARGS = {"json": {"name":"test_metadata_put"}}
NOT_VALID_LIST_ARGS = "not_valid_data"


class TestMetadataResource(BasicIntegrationTest):

    def testMetadataResourceGet(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(NOT_VALID_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE_GET)

    def testMetadataResourcePut(self):
        response = requests.put(self.getUrl(TEST_URL), data=LIST_ARGS)
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.put(self.getUrl(NOT_VALID_URL), data=NOT_VALID_LIST_ARGS)
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
