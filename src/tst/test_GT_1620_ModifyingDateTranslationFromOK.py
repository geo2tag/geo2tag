from unittest import TestCase
from datetime import datetime
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator
from open_karelia_object_to_point_translator import date_name_to_datetime
from open_karelia_object_to_point_translator import key_in_dict_and_defined
from open_karelia_object_to_point_translator import add_precise_or_interval_to_point
from open_karelia_object_to_point_translator import define_date_type
from open_karelia_object_to_point_translator import DATE_TYPES

TEST_DATA = [
    {'image_url': 'image_url', 'object_url': 'object_url'},
    {
        'name': ['test_GT_1620'],
        '_id': '111',
        'latitude': 1,
        'longitude': 2,
    },
    'test_version',
    'test_import',
    'channelId'
]


class TestModifyigDateTranslationFromOK(TestCase):
    def testModifyigDateTranslationFromOK_JustDate(self):
        td = OpenKareliaObjectToPointTranslator(None, {}, None, None, None).translateDate()
        self.assertEqual(td[0].replace(microsecond=0), datetime.now().replace(microsecond=0))
        self.assertEqual(td[1], False)

    def testModifyigDateTranslationFromOK_PresiseDate(self):
        td = OpenKareliaObjectToPointTranslator(None, {'year': 2000, 'bc': True}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], True)
        td = OpenKareliaObjectToPointTranslator(None, {'century': 20}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)
        td = OpenKareliaObjectToPointTranslator(None, {'millenium': 2}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)

    def testModifyigDateTranslationFromOK_IntervalDates(self):
        td = OpenKareliaObjectToPointTranslator(None, {'year_start': 2000, 'year_end': 3000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
        td = OpenKareliaObjectToPointTranslator(None, {'century_start': 20, 'century_end': 30}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
        td = OpenKareliaObjectToPointTranslator(None, {'millenium_start': 2, 'millenium_end': 3}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)

    def testModifyigDateTranslationFromOK_MixedDateTypes(self):
        td = OpenKareliaObjectToPointTranslator(None, {'year': 1000, 'year_start': 2000, 'year_end': 3000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
        td = OpenKareliaObjectToPointTranslator(None, {'century': 20, 'year_end': 3000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)
        td = OpenKareliaObjectToPointTranslator( None, {'millenium': 4, 'century': 20, 'year': 3000}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td[1], False)
        td = OpenKareliaObjectToPointTranslator(None, {'millenium_start': 2, 'millenium_end': 3, 'year_start': 4000, 'year_end': 5000, 'century_start': 60, 'century_end': 70}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(4000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(5000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)
        td = OpenKareliaObjectToPointTranslator(None, {'millenium_start': 2, 'millenium_end': 3, 'century_start': 40, 'century_end': 50}, None, None, None).translateDate()
        self.assertEqual(td[0], datetime(4000, 1, 1, 0, 0))
        self.assertEqual(td[1], datetime(5000, 1, 1, 0, 0))
        self.assertEqual(td[2], False)
        self.assertEqual(td[3], False)

    def testModifyigDateTrnaslationFromOK_GetPointFunc(self):
        TEST_DATA[1]['bc'] = True
        td = OpenKareliaObjectToPointTranslator(TEST_DATA[0], TEST_DATA[1], TEST_DATA[2], TEST_DATA[3], TEST_DATA[4]).getPoint()
        self.assertEqual(td['date'].replace(microsecond=0), datetime.now().replace(microsecond=0))
        # Next line is assertation for False because date was not set
        self.assertEqual(td['bc'], False)
        TEST_DATA[1]['year_start'] = 2000
        TEST_DATA[1]['year_end'] = 3000
        TEST_DATA[1]['bc_start'] = False
        TEST_DATA[1]['bc_end'] = False
        td = OpenKareliaObjectToPointTranslator(TEST_DATA[0], TEST_DATA[1], TEST_DATA[2], TEST_DATA[3], TEST_DATA[4]).getPoint()
        self.assertEqual(td['date'], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(td['json']['date'], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(td['bc'], False)
        self.assertEqual(td['json']['bc'], False)

    def testModifyigDateTrnaslationFromOK_DateNameToDatetime(self):
        self.assertEqual(date_name_to_datetime({'year': 2000}, 'year'), datetime(2000, 1, 1, 0, 0))
        self.assertEqual(date_name_to_datetime({'century': 20}, 'century'), datetime(2000, 1, 1, 0, 0))
        self.assertEqual(date_name_to_datetime({'millenium':    2}, 'millenium'), datetime(2000, 1, 1, 0, 0))
        self.assertEqual(date_name_to_datetime({'year_start': 2000}, 'year_start'), datetime(2000, 1, 1, 0, 0))
        self.assertEqual(date_name_to_datetime({'century_start': 20}, 'century_start'), datetime(2000, 1, 1, 0, 0))
        self.assertEqual(date_name_to_datetime({'millenium_start':    2}, 'millenium_start'), datetime(2000, 1, 1, 0, 0))
        self.assertEqual(date_name_to_datetime({'year_end': 2000}, 'year_end'), datetime(2000, 1, 1, 0, 0))
        self.assertEqual(date_name_to_datetime({'century_end': 20}, 'century_end'), datetime(2000, 1, 1, 0, 0))
        self.assertEqual(date_name_to_datetime({'millenium_end':    2}, 'millenium_end'), datetime(2000, 1, 1, 0, 0))

    def testModifyigDateTrnaslationFromOK_KeyInDictAndDefined(self):
        self.assertEqual(key_in_dict_and_defined('test', {'test': 'test'}), True)
        self.assertEqual(key_in_dict_and_defined('test', {}), False)

    def testModifyigDateTrnaslationFromOK_AddPreciseOrIntervalToPoint(self):
        point = {}
        add_precise_or_interval_to_point((datetime(2000, 1, 1, 0, 0), True), point)
        self.assertEqual(point['date'], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(point['bc'], True)
        point = {'json': {}}
        add_precise_or_interval_to_point((
            datetime(2000, 1, 1, 0, 0),
            datetime(3000, 1, 1, 0, 0),
            True,
            True
        ), point)
        self.assertEqual(point['date'], datetime(2000, 1, 1, 0, 0))
        self.assertEqual(point['json']['date'], datetime(3000, 1, 1, 0, 0))
        self.assertEqual(point['bc'], True)
        self.assertEqual(point['json']['bc'], True)
    def testModifyigDateTrnaslationFromOK_DefineDateType(self):
    	self.assertEqual(define_date_type({'year': 1000}), (DATE_TYPES[1], 0))
    	self.assertEqual(define_date_type({'century': 10}), (DATE_TYPES[1], 1))
    	self.assertEqual(define_date_type({'millenium': 1}), (DATE_TYPES[1], 2))
    	self.assertEqual(define_date_type({'year_start': 1000, 'year_end': 2000}), (DATE_TYPES[0], 0))
    	self.assertEqual(define_date_type({'century_start': 10, 'century_end': 20}), (DATE_TYPES[0], 1))
    	self.assertEqual(define_date_type({'millenium_start': 1, 'millenium_end': 2}), (DATE_TYPES[0], 2))


