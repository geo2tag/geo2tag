import requests
from basic_integration_test import BasicIntegrationTest

URL = '/instance/status'

LOG = 'log'
ID = '_id'

LOG_URL = '/instance/log?number=1'


class TestAfterRequestStatusLogging(BasicIntegrationTest):

    def testAfterRequestStatusLogging(self):
        requests.get(self.getUrl(URL))
        response = requests.get(self.getUrl(LOG_URL))
        self.assertEqual(response.status_code, 200)
