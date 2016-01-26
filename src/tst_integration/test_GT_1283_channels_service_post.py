import requests
from basic_integration_test import BasicIntegrationTest
import json

TEST_URL = '/instance/service/testservice/channel'
TEST_SERVICE = 'testservice'
NAME = 'tes t_name'
JSON = "{'1': 2, '2': '4'}"
JSON2 = [1, 2, 3]
DATA = {'name': NAME, 'json': JSON}
DATA2 = {'name': 123}
ID_KEY = u'$oid'


class TestChannelServicePostRequest(BasicIntegrationTest):

    def testChannelServicePostRequest(self):
        response = requests.post(self.getUrl(TEST_URL), data=DATA)
        responseText = response.text
        responseCode = response.status_code
        ID = json.loads(responseText)
        response = requests.delete(self.getUrl(TEST_URL + '/' + ID[ID_KEY]))  
        self.assertNotEquals(responseText, [])
        self.assertNotEquals(responseText, {})
        self.assertEquals(responseCode, 200)
        response = requests.post(self.getUrl(TEST_URL), data=DATA2)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, 400)
