import unittest
import sys
sys.path.append('../')
from db_model import findPoints
import dateutil.parser
from bson.objectid import ObjectId

TEST_SERVICE = 'testservice'

TEST_CHANNELS = [
    ObjectId("556721a52a2e7febd2744206")]
TEST_NUMBER = 100


class TestApplydateCriterion(unittest.TestCase):

    def testApplydateCriterion2(self):
        TEST_DATE_FROM = dateutil.parser.parse("1000")
        TEST_DATE_TO = dateutil.parser.parse("1200")
        result_1 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                TEST_DATE_TO,
                TEST_DATE_FROM,
                None,
                None,
                True,
                False
                ))
        result_2 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                TEST_DATE_TO,
                TEST_DATE_FROM,
                None,
                None,
                True,
                True
                ))
        result_3 = list(
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
                False,
                False
                ))
        result_4 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                None,
                TEST_DATE_TO
                ))
        result_5 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                TEST_DATE_TO,
                None
                ))
        result_6 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                None,
                TEST_DATE_FROM,
                None,
                None,
                None,
                True
                ))
        result_7 = list(
            findPoints(
                TEST_SERVICE,
                TEST_CHANNELS,
                TEST_NUMBER,
                None,
                None,
                None,
                None,
                TEST_DATE_FROM,
                None,
                None,
                None,
                True
                ))
        self.assertEquals(len(result_1), 3)
        self.assertEquals(len(result_2), 1)
        self.assertEquals(len(result_3), 1)
        self.assertEquals(len(result_4), 4)
        self.assertEquals(len(result_5), 1)
        self.assertEquals(len(result_6), 1)
        self.assertEquals(len(result_7), 4)