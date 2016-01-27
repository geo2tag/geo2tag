import requests
from json import loads
from basic_integration_test import BasicIntegrationTest

URL = '/instance/status'

LOG = 'log'
ID = '_id'

MESSAGE_FIELD = 'message'
MESSAGE = 'Status_code: 200, response: [\'OK\']'
LOG_URL = '/instance/log?number=1'


class TestAfterRequestStatusLogging(BasicIntegrationTest):

    def testAfterRequestStatusLogging(self):
        requests.get(self.getUrl(URL))
        response = requests.get(self.getUrl(LOG_URL))
        logEntries = loads(response.text)
        lastEntry = logEntries[0]
        self.assertEqual(lastEntry[MESSAGE_FIELD], MESSAGE)
