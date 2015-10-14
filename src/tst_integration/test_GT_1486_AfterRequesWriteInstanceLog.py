import requests
from datetime import datetime
from basic_integration_test import BasicIntegrationTest
from url_routines import getInstancePrefix


URL_STATUS = '/' + getInstancePrefix() + '/status'
URL_INSTANCE_LOG = '/' + getInstancePrefix() + '/log'
MESSAGE_FIELD = 'message'
VALID_MESSAGE = 'Request url: http://geomongo/instance/status, request data: '


class TestAfterRequestWriteInstanceLog(BasicIntegrationTest):

    def testAfterRequestWriteInstanceLog(self):
        datetime_from = datetime.now()
        requests.get(self.getUrl(URL_STATUS))
        datetime_to = datetime.now()
        r = requests.get(self.getUrl(URL_INSTANCE_LOG),
                         params={
                             'number': 0,
                             'offset': 0,
                             'date_from': str(datetime_from.isoformat()),
                             'date_to': str(datetime_to.isoformat())
        })
        import ast
        self.assertEqual(
            ast.literal_eval(
                r.text)[0][MESSAGE_FIELD],
            VALID_MESSAGE)
