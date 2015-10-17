import unittest
import requests
from jobs_creator import createImportJob
TEST_URL = 'http://httpbin.org/status/200'
TEST_DATA = '{}'


class TestJobsCreator(unittest.TestCase):

    def testJobsCreator(self):

        self.assertEquals(
            createImportJob(TEST_URL, TEST_DATA).status_code, 200)
