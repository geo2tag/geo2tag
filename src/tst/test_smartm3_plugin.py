# -*- coding: utf-8 -*-

from unittest import TestCase, TestSuite, TextTestRunner
from sys import exit
from jsonld_converter import convertPointToJsonLD, \
    convertPointsToJsonLD
from db_model import getPointById

TEST_SERVICE = 'testservice'
TEST_POINT_ID = '55a624c69bf999b58a366f10'
VALID_POINT = {'bc': False, 'altitude': 1, 'longitude': 0, 
               'channel_id': u'556721a52a2e7febd2744200', 
               'json': {}, 'date': '2015-09-10T23:32:17.814000', 
               'latitude': 0, 
               'point_id': u'55a624c69bf999b58a366f10',
               '@context': '/instance/plugins/smartm3/point.jsonld'}
VALID_LIST = [VALID_POINT]


class TestSmartM3Plugin(TestCase):

    def testJsonLDConversion(self):
        TEST_POINT = getPointById (TEST_SERVICE, TEST_POINT_ID)
        convertedPoint = convertPointToJsonLD(TEST_POINT)
        self.assertEquals(convertedPoint, VALID_POINT)

        TEST_LIST = [TEST_POINT]
        convertedList = convertPointsToJsonLD(TEST_LIST)
        self.assertEquals(convertedList, VALID_LIST)

if __name__ == '__main__':
    suite = TestSuite()
    returnCode = not TextTestRunner(
        verbosity=2).run(suite).wasSuccessful()

    exit(returnCode)


