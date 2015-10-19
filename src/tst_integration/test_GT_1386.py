import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/status'


class Test_GT_1386(BasicIntegrationTest):

    def test_GT_1386(self):
        response = requests.get(self.getUrl(TEST_URL))
        self.assertEquals(
            response.headers['access-control-allow-methods'],
            'GET, POST, PUT, DELETE')
        self.assertEquals(response.headers['access-control-allow-origin'], '*')
        self.assertEquals(
            response.headers['access-control-allow-headers'],
            'Content-Type, Authorization')
