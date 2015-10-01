from unittest import TestCase

"""import sys
sys.path.append('../')
sys.path.append('../plugins/geocoder/')"""

from geocoding_job import GeocodingJob
from db_model import getDbObject
from pymongo import DESCENDING
import time


CHANNEL_NAME = 'channelName'
SERVICE_NAME = 'serviceName'

TEST_DATA_FIELD = 'test_data_GT_1705'

log = getDbObject('testservice')['log']


def bcgFunc(self, channelName, serviceName):
    log.insert({'test_data_GT_1705': [channelName, serviceName]})

gj = GeocodingJob(bcgFunc, 'channelName', None, None, 'serviceName')


class TestGeocodingJob(TestCase):
    def testGeocodingJob(self):
        gj.internalStart()
        self.assertIsNotNone(gj.thread)
        self.assertTrue(gj.thread.is_alive())
        """gj.internalStop()
        self.assertFalse(gj.thread.is_alive())"""
        time.sleep(5)
        resList = list(log.find().sort('_id', DESCENDING))
        self.assertTrue(TEST_DATA_FIELD in resList[0])
        self.assertEqual(
            resList[0][TEST_DATA_FIELD],
            [CHANNEL_NAME, SERVICE_NAME]
        )



