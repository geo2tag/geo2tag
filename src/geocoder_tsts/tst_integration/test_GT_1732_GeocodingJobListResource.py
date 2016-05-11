from basic_integration_test import BasicIntegrationTest
import requests
import json


class TestGeocodingJobListResource(BasicIntegrationTest):

    def testGeocodingJobListResource(self):
        r = requests.get(
            self.getUrl(
                '/instance/plugin/geocoder/service/testservice/job'
            )
        )
        print r.text
        self.assertEqual(type(json.loads(r.text)), list)
        self.assertEqual(r.status_code, 200)
