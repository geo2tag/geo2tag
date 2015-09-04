import unittest
import sys
sys.path.append('../')
from db_model import findPoints
import dateutil.parser
from bson.objectid import ObjectId

TEST_SERVICE = 'testservice'

#(112, 9, 18, 22, 13, 20) -58610224000000
#(1063, 5, 19, 3, 33, 20) -28610224000000
TEST_CHANNELS = [
    ObjectId("556721a52a2e7febd2744203")]
TEST_NUMBER = 100


class TestApplydateCriterion(unittest.TestCase):

    def testApplydateCriterion2(self):
        TEST_DATE_FROM = dateutil.parser.parse("1000")
        TEST_DATE_TO = dateutil.parser.parse("1200")
        '''result_1 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                TEST_DATE_FROM,
                TEST_DATE_TO))
        result_2 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                TEST_DATE_FROM,
                None))
        result_3 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                TEST_DATE_TO,
                None))'''
        result_2 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                TEST_DATE_FROM,
                TEST_DATE_TO,
                None,
                None,
                True,
                False
                ))
        print
        print
        print result_2