import unittest
import sys
sys.path.append('../')
from db_model import findPoints
from bson.objectid import ObjectId

TEST_SERVICE = 'testservice'
TEST_CHANNEL = [ObjectId("55dc620fbe9b3bf61be83f93")]
TEST_NUMBER = 1000
JSON = 'json'
IMAGE_URL = 'image_url'
HTTP_KEYWORD_TO_TEST = 'http'


class TestKareliaObjectsImageUrl(unittest.TestCase):

    def testKareliaObjectsImageUrl(self):
        result = list(findPoints(TEST_SERVICE, TEST_CHANNEL, TEST_NUMBER))
        for i in result:    
            self.assertEquals( HTTP_KEYWORD_TO_TEST in i[JSON][IMAGE_URL], True)