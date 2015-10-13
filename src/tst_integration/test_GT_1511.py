import requests
import json
from basic_integration_test import BasicIntegrationTest

TEST_URL = 'instance/plugin/ok_import/service/testservice/job'
VALID_RESPONSE_CODE = 200
DATA_ARR = ['channelName', 'openDataUrl', 'showObjectUrl', 'showImageUrl']
TEST_VAL_PREFIX = 'test_val_'
CHANNELNAME = 'testchannel'
DATA = {
    DATA_ARR[0]: CHANNELNAME,
    DATA_ARR[1]: TEST_VAL_PREFIX + DATA_ARR[1],
    DATA_ARR[2]: TEST_VAL_PREFIX + DATA_ARR[2],
    DATA_ARR[3]: TEST_VAL_PREFIX + DATA_ARR[3]
}


class Test_GT_1511(BasicIntegrationTest):

    def test_GT_1511(self):
        response = requests.post(self.getUrl(TEST_URL), data=json.dumps(DATA))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(len(responseText), 12)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        TEST_URL2 = 'instance/plugin/ok_import/service/testservice/job/' + responseText
        response = requests.get(self.getUrl(TEST_URL2))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(type(responseText), unicode)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        dictJobDescription = json.loads(responseText)
        self.assertEquals(type(dictJobDescription), dict)
        for arg in DATA_ARR:
            self.assertTrue(arg in dict(dictJobDescription).keys())
        response = requests.delete(self.getUrl(TEST_URL2))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, 'null')
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
