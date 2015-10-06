from unittest import TestCase
from geocoding_job import GeocodingJob
from db_model import getDbObject
from pymongo import DESCENDING
from time import sleep



CHANNEL_NAME = 'channelName'
SERVICE_NAME = 'serviceName'

TEST_DATA_FIELD = 'test_data_GT_1705'

log = getDbObject('testservice')['log']


def bcgFunc(self, channelName, serviceName):
    log.insert({'test_data_GT_1705': [channelName, serviceName]})

gj = GeocodingJob(bcgFunc, 'channelName', None, None, 'serviceName')


class TestGeocodingJob(TestCase):
    def testGeocodingJob(self):
        gj.start()
        self.assertIsNotNone(gj.thread)
        self.assertTrue(gj.thread.is_alive())
        gj.stop()
        if gj.thread.is_alive():
            while gj.thread.is_alive():
                print gj.thread.is_alive()
                sleep(0.1)
        self.assertFalse(gj.thread.is_alive())
        self.assertTrue(gj.done)
        res_list = list(log.find().sort('_id', DESCENDING))
        self.assertTrue(TEST_DATA_FIELD in res_list[0])
        self.assertEqual(
            res_list[0][TEST_DATA_FIELD],
            [CHANNEL_NAME, SERVICE_NAME]
        )
        discr = gj.describe()
        self.assertEqual(discr[CHANNEL_NAME], CHANNEL_NAME)
        self.assertEqual(discr[SERVICE_NAME], SERVICE_NAME)