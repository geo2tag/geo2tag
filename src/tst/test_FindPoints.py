import unittest
import sys
sys.path.append('../')
from db_model import findPoints
import dateutil.parser
from bson.objectid import ObjectId

TEST_SERVICE = 'testservice'


TEST_CHANNELS = [ObjectId("556721a52a2e7febd2744201"), ObjectId("556721a52a2e7febd2744202")]
TEST_NUMBER = 100

class TestFindpoints(unittest.TestCase):
    
    def testChannelSearch(self):
        VALID_RESULTS_NUMBER = 4
        result = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER))
        self.assertEquals(VALID_RESULTS_NUMBER, len(result))

    def testDateSearch(self):
        TEST_DATE_FROM = dateutil.parser.parse("2015-09-10T23:32:17.814Z")
        TEST_DATE_FROM_1 = dateutil.parser.parse("2015-09-11T23:32:16.814Z")
        TEST_DATE_TO = dateutil.parser.parse("2015-09-11T23:32:17.814Z")
        TEST_DATE_TO_1 = dateutil.parser.parse("2015-09-11T23:32:16.814Z")
        VALID_RESULTS_NUMBER_1 = 4
        VALID_RESULTS_NUMBER_2 = 3
        VALID_RESULTS_NUMBER_3 = 1
        

        result_1 = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER, None, \
            None, None, None,  TEST_DATE_FROM, TEST_DATE_TO))
        result_2 = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER, None, \
            None, None, None, None, TEST_DATE_TO_1))
        result_3 = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER, None, \
            None, None, None, TEST_DATE_FROM_1))
        self.assertEquals(VALID_RESULTS_NUMBER_1, len(result_1)) 
        self.assertEquals(VALID_RESULTS_NUMBER_2, len(result_2)) 
        self.assertEquals(VALID_RESULTS_NUMBER_3, len(result_3)) 

    def testAltitudeSearch(self):
        TEST_ALT_FROM = 1
        TEST_ALT_FROM1 = 2

        TEST_ALT_TO = 2
        TEST_ALT_TO1 = 1  

        VALID_RESULTS_NUMBER_1 = 4
        VALID_RESULTS_NUMBER_2 = 2
        VALID_RESULTS_NUMBER_3 = 2

        result_1 = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER, None, \
            TEST_ALT_FROM, TEST_ALT_TO))
        result_2 = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER, None, \
            TEST_ALT_FROM1))
        result_3 = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER, None, \
            None, TEST_ALT_TO1))
        self.assertEquals(VALID_RESULTS_NUMBER_1, len(result_1)) 
        self.assertEquals(VALID_RESULTS_NUMBER_2, len(result_2)) 
        self.assertEquals(VALID_RESULTS_NUMBER_3, len(result_3)) 


    def testGeometrySearch(self):
        TEST_GEOMETRY_P = {'type': 'Polygon', 'coordinates':  
            [ [[ 0.9, 0.9 ], [ 0.9, 1.1 ], [ 1.4, 1.1 ],  [ 1.4, 0.9 ], [ 0.9, 0.9 ] ]] }
        TEST_GEOMETRY_C = {'type': 'Point', 'coordinates': [1, 1]}
        TEST_RADIUS = 0.003

        VALID_RESULTS_NUMBER_1 = 3
        VALID_RESULTS_NUMBER_2 = 2

        result_1 = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER, TEST_GEOMETRY_P))
        result_2 = list(findPoints(TEST_SERVICE, TEST_CHANNELS, TEST_NUMBER, TEST_GEOMETRY_C, \
            None, None, None, None, None, None, TEST_RADIUS))

        self.assertEquals(VALID_RESULTS_NUMBER_1, len(result_1)) 
        self.assertEquals(VALID_RESULTS_NUMBER_2, len(result_2)) 
