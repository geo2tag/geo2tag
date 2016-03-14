import requests
from datetime import datetime
from basic_integration_test import BasicIntegrationTest
from url_routines import getInstancePrefix

URL_STATUS = '/' + getInstancePrefix() + '/status'
URL_INSTANCE_LOG = '/' + getInstancePrefix() + '/log'


class TestAfterRequestWriteInstanceLog(BasicIntegrationTest):

    def testAfterRequestWriteInstanceLog(self):
        datetime_from = datetime.now()
        requests.get(self.getUrl(URL_STATUS))
        datetime_to = datetime.now()
        r = requests.get(self.getUrl(URL_INSTANCE_LOG),
                         params={
                             'number': 0,
                             'offset': 0,
                             'date_from': unicode(datetime_from.isoformat()),
                             'date_to': unicode(datetime_to.isoformat())
        })
        self.assertEqual(r.status_code, 200)
