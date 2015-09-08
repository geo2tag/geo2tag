from unittest import TestCase
from datetime import datetime
import sys
sys.path.append('../plugins/ok_import/')
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator

TEST_DATA = [
    'image_url',
    'object_url',
    {
        'name': ['test_GT_1499'],
        '_id': '111',
        'latitude': 1,
        'longitude': 2
    },
    'test_version',
    'test_import',
    'channelId'
]

class TestModifyigDateTrnslationFromOK(TestCase):
    def testModifyigDateTrnslationFromOK_JustDate(self):
        td = OpenKareliaObjectToPointTranslator(None, None, {}, None, None, None).translateDate()
        self.assertEqual(td.replace(microsecond=0), datetime.now().replace(microsecond=0))
    def testModifyigDateTrnslationFromOK_PresiseDate(self):
        td = OpenKareliaObjectToPointTranslator(None, None, {'year': 2000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)
        td = OpenKareliaObjectToPointTranslator(None, None, {'century': 20}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)
        td = OpenKareliaObjectToPointTranslator(None, None, {'millenium': 2}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)
    def testModifyigDateTrnslationFromOK_IntervalDates(self):
        td = OpenKareliaObjectToPointTranslator(None, None, {'year_start': 2000, 'year_end': 3000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
        td = OpenKareliaObjectToPointTranslator(None, None, {'century_start': 20, 'century_end': 30}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
        td = OpenKareliaObjectToPointTranslator(None, None, {'millenium_start': 2, 'millenium_end': 3}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
    def testModifyigDateTrnslationFromOK_MixedDateTypes(self):
        td = OpenKareliaObjectToPointTranslator(None, None, {'year': 1000, 'year_start': 2000, 'year_end': 3000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
        td = OpenKareliaObjectToPointTranslator(None, None, {'century': 20, 'year_end': 3000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)
        td = OpenKareliaObjectToPointTranslator(None, None, {'millenium': 4, 'century': 20, 'year': 3000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)
        td = OpenKareliaObjectToPointTranslator(None, None, {'millenium_start': 2, 'millenium_end': 3, 'year_start': 4000, 'year_end': 5000, 'century_start': 60, 'century_end': 70}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(4000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(5000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
        td = OpenKareliaObjectToPointTranslator(None, None, {'millenium_start': 2, 'millenium_end': 3, 'century_start': 40, 'century_end': 50}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(4000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(5000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
    def testModifyigDateTrnslationFromOK_RealRequestData(self):
        import requests
        import json
        r = requests.get("http://mobile.openkarelia.org/get_nearest_objects?latitude=61.787458487564&longitude=34.362810647964")
        js_r = json.loads(r.text)[0]
        self.assertEqual(
            OpenKareliaObjectToPointTranslator(None, None, js_r, None, None, None).translateDate(),
            (datetime(1900, 1, 1, 0, 0), datetime(1900, 1, 1, 0, 0), False, False)
        )
    def testModifyigDateTrnslationFromOK_GetPointFunc(self):
        td = OpenKareliaObjectToPointTranslator(TEST_DATA[0], TEST_DATA[1], TEST_DATA[2], TEST_DATA[3], TEST_DATA[4], TEST_DATA[5]).getPoint()
        self.assertEqual(td['date'].replace(microsecond=0), datetime.now().replace(microsecond=0))
        self.assertEqual(td['bc'], False)
        TEST_DATA[2]['year_start'] = 2000
        TEST_DATA[2]['year_end'] = 3000
        td = OpenKareliaObjectToPointTranslator(TEST_DATA[0], TEST_DATA[1], TEST_DATA[2], TEST_DATA[3], TEST_DATA[4], TEST_DATA[5]).getPoint()
        self.assertEqual(td['date'], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td['json']['date'], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td['bc'], False)
        self.assertEqual(td['json']['bc'], False)
