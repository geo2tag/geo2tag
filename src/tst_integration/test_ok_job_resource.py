import unittest
import requests
import json
from basic_integration_test import BasicIntegrationTest

TEST_URL = 'instance/plugin/ok_import/service/testservice/job'
VALID_RESPONSE_CODE = 200
DATA_ARR = ['channelName', 'openDataUrl', 'showObjectUrl', 'showImageUrl']
TEST_VAL_PREFIX = 'test_val_'
DATA = {
    DATA_ARR[0]: TEST_VAL_PREFIX + DATA_ARR[0],
    DATA_ARR[1]: TEST_VAL_PREFIX + DATA_ARR[1],
    DATA_ARR[2]: TEST_VAL_PREFIX + DATA_ARR[2],
    DATA_ARR[3]: TEST_VAL_PREFIX + DATA_ARR[3]
}

class Test_OKImportJob(BasicIntegrationTest):
    def test_OKImportJob(self):
        response = requests.post(self.getUrl(TEST_URL), data = DATA)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(len(responseText), 12)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL))
        responseList = json.loads(response.text)
        self.assertIsInstance(responseList, list)
        self.assertNotEquals( len(responseList), 0)
