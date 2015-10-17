from basic_integration_test import BasicIntegrationTest
import requests

URL = '/instance/service/testservice/point'

NO_BC_ERR_DATA = {
    'number': '10',
    'channel_ids': '556721a52a2e7febd2744201',
    'date_from': '1970-09-10T01:01:01.000000',
    'date_to': '2100-09-10T01:01:01.000000'
}

NO_BC_TO_ERR_DATA = NO_BC_ERR_DATA.copy()
NO_BC_TO_ERR_DATA['bc_from'] = 'true'

NO_BC_FROM_ERR_DATA = NO_BC_ERR_DATA.copy()
NO_BC_FROM_ERR_DATA['bc_to'] = 'true'

NO_DATE_DATA = NO_BC_ERR_DATA.copy()
NO_DATE_DATA.pop('date_from', None)
NO_DATE_DATA.pop('date_to', None)

DATE_AND_BC_FLAGS = NO_BC_ERR_DATA.copy()
DATE_AND_BC_FLAGS['bc_from'] = 'true'
DATE_AND_BC_FLAGS['bc_to'] = 'true'

BC_FROM = '[bc_from] '
BC_TO = '[bc_to] '

ERR_MSG_KEY = '{"message": "'
ERR_MSG = ': Missing required parameter in the JSON body ' \
          'or the post body or the query string"}'

BAD_REQUEST = 400
OK = 200

NO_BC_ERR_DATA_RESP_TEXT = ERR_MSG_KEY + BC_FROM + BC_TO + ERR_MSG
NO_BC_TO_ERR_DATA_RESP_TEXT = ERR_MSG_KEY + BC_TO + ERR_MSG
NO_BC_FROM_ERR_DATA_RESP_TEXT = ERR_MSG_KEY + BC_FROM + ERR_MSG
NO_DATE_DATA_RESP_TEXT = \
    '[{"bc": false, ' \
    '"channel_id": {"$oid": "556721a52a2e7febd2744201"},' \
    ' "json": {"image_url": "http://www.dunbartutoring.com/' \
    'wp-content/themes/thesis/rotator/sample-1.jpg", ' \
    '"description": "testGT-1332"},' \
    ' "location": {"type": "Point", "coordinates": [1, 1]}, ' \
    '"date": {"$date": 1441927937814}, "alt": 1, ' \
    '"_id": {"$oid": "55a624c09bf770b58a355f07"}},' \
    ' {"bc": false, "channel_id": {"$oid": "556721a52a2e7febd2744201"}, ' \
    '"json": {"image_url": ' \
    '"https://www.drupal.org/files/hr10_sample_image_02_original.jpg",' \
    ' "description": "testGT-1332"}, "location": {"type": "Point",' \
    ' "coordinates": [1, 1]}, "date": {"$date": 1441927937814},' \
    ' "alt": 2, "_id": {"$oid": "55a624c69bf770b58a355f08"}}]'
DATE_AND_BC_FLAGS_RESP_TEXT = NO_DATE_DATA_RESP_TEXT


class TestExtendPointListParserWithFlagsBC(BasicIntegrationTest):

    def testExtendPointListParserWithFlagsBC_DATES_NO_BC(self):
        r = requests.get(self.getUrl(URL), data=NO_BC_ERR_DATA)
        self.assertEqual(r.status_code, BAD_REQUEST)
        self.assertEqual(r.text, NO_BC_ERR_DATA_RESP_TEXT)

    def testExtendPointListParserWithFlagsBC_DATES_NO_BC_TO(self):
        r = requests.get(self.getUrl(URL), data=NO_BC_TO_ERR_DATA)
        self.assertEqual(r.status_code, BAD_REQUEST)
        self.assertEqual(r.text, NO_BC_TO_ERR_DATA_RESP_TEXT)

    def testExtendPointListParserWithFlagsBC_DATES_NO_BC_FROM(self):
        r = requests.get(self.getUrl(URL), data=NO_BC_FROM_ERR_DATA)
        self.assertEqual(r.status_code, BAD_REQUEST)
        self.assertEqual(r.text, NO_BC_FROM_ERR_DATA_RESP_TEXT)

    def testExtendPointListParserWithFlagsBC_NO_DATES(self):
        r = requests.get(self.getUrl(URL), data=NO_DATE_DATA)
        self.assertEqual(r.status_code, OK)
        self.assertEqual(r.text, NO_DATE_DATA_RESP_TEXT)

    def testExtendPointListParserWithFlagsBC_DATES_BC_FROM_BC_TO(self):
        r = requests.get(self.getUrl(URL), data=DATE_AND_BC_FLAGS)
        self.assertEqual(r.status_code, OK)
        self.assertEqual(r.text, DATE_AND_BC_FLAGS_RESP_TEXT)
