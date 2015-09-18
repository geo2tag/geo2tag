from unittest import TestCase
from json import dumps, loads
import requests
import sys
sys.path.append("../geocoders")
from geocoder_response_parser import GeocoderResponseParser, field_in_dict_and_defined
from geocoder_response_parser import TOTAL_RESULTS_COUNT, GEONAMES, LAT, LNG

DATA_URL = "http://api.geonames.org/searchJSON?q=london&username=geo2tag"

DATA_JSON = {
    GEONAMES: []
}


class TestGeocoderResponseParser(TestCase):
    def testGeocoderResponseParser_parseSinge(self):
        res = GeocoderResponseParser.parseSingle(dumps(DATA_JSON))
        self.assertEqual(res, None)
        DATA_JSON[TOTAL_RESULTS_COUNT] = 0
        res = GeocoderResponseParser.parseSingle(dumps(DATA_JSON))
        self.assertEqual(res, None)
        DATA_JSON[GEONAMES] = [{LAT: 2, LNG:5}]
        DATA_JSON[TOTAL_RESULTS_COUNT] = 1
        res = GeocoderResponseParser.parseSingle(dumps(DATA_JSON))
        DATA_JSON[GEONAMES] = [{LAT: 2, LNG: 5}, {LAT: 3, LNG: 4}]
        DATA_JSON[TOTAL_RESULTS_COUNT] = 2
        res = GeocoderResponseParser.parseSingle(dumps(DATA_JSON))
        self.assertEqual(res, [[2, 5], [3, 4]])
        DATA_JSON[GEONAMES] = [{LAT: 2}, {LNG: 4}]
        DATA_JSON[TOTAL_RESULTS_COUNT] = 2
        res = GeocoderResponseParser.parseSingle(dumps(DATA_JSON))
        self.assertEqual(res, None)

    def testGeocoderResponseParser_parseText(self):
        res = GeocoderResponseParser.parseList([])
        self.assertEqual(res, None)
        DATA_JSON[GEONAMES] = [{LAT: 2, LNG: 5}, {LAT: 3, LNG: 4}]
        DATA_JSON[TOTAL_RESULTS_COUNT] = 2
        res = GeocoderResponseParser.parseList([dumps(DATA_JSON), dumps(DATA_JSON)])
        self.assertEqual(res, [[2, 5], [3, 4], [2, 5], [3, 4]])

    def testGeocoderResponseParser_parseText_RealReauest(self):
        r = requests.get(DATA_URL)
        self.assertTrue(loads(r.text)[TOTAL_RESULTS_COUNT] > 0)
        self.assertTrue(len(loads(r.text)[GEONAMES]) > 0)

    def testGeocoderResponseParser_fieldInDictAndDefined(self):
        self.assertTrue(field_in_dict_and_defined("field", {"field": "defined"}))
        self.assertFalse(field_in_dict_and_defined("field", {"field": None}))
        self.assertFalse(field_in_dict_and_defined("field", {}))



