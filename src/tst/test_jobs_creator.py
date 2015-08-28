import unittest
import sys
import requests
sys.path.append('../performance/od_performance/')
from jobs_creator import createImportJob
TEST_URL = u'http://geomongo/instance/plugin/ok_import/service/testservice/job'
TEST_DATA = u'{"channelName":"test_GT_1286","openDataUrl":"http://mobile.openkarelia.org//get_nearest_objects?latitude=61.787458487564&longitude=34.362810647964", "showObjectUrl":"", "showImageUrl":""}'
RESPONSE = '<Response [200]>'


class TestJobsCreator(unittest.TestCase):

    def testJobsCreator(self):
        self.assertEquals(
            str(createImportJob(TEST_URL, TEST_DATA)), RESPONSE)
