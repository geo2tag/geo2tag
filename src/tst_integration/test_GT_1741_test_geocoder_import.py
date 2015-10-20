from config_reader import getGeonamesLogin
from basic_integration_test import BasicIntegrationTest
import json
import requests
from configparser import RawConfigParser
import time

GET_POST_JOB_URL = 'instance/plugin/geocoder/service/testservice/job'
POST_IMPORT_DATA = {'channelName': 'geocoder_plugin_test_channel'}
GET_POINTS_URL = 'instance/service/testservice/point?number=' \
                 '1000&channel_ids=556721a52a2e7febd2744307'
DATA_FILE = 'geocoding_data_test_after_import.txt'
DONE = 'done'


class TestGeocoderImport(BasicIntegrationTest):
    def testGeocoderImport(self):
        jobId = requests.post(
            self.getUrl(GET_POST_JOB_URL),
            data=json.dumps(POST_IMPORT_DATA)
        )
        jobJson = json.loads(
            requests.get(
                self.getUrl(GET_POST_JOB_URL + '/' + jobId.text)
            ).text
        )
        while jobJson[DONE] is not True:
            jobJson = json.loads(
                requests.get(
                    self.getUrl(GET_POST_JOB_URL + '/' + jobId.text)
                ).text
            )
            print jobJson
            time.sleep(0.5)
        self.assertTrue(jobJson[DONE])
        f = open(DATA_FILE, 'r')
        fout = f.read()
        self.assertEqual(
            requests.get(self.getUrl(GET_POINTS_URL)).text,
            fout
        )
