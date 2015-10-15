from configparser import RawConfigParser
from bson import ObjectId
from db_model import getServiceIdByName, getChannelByName, getDbObject
from config_reader import getGeonamesLogin
from geocoder_import import geocoderImport
from unittest import TestCase

CHANNEL_NAME = 'geocoder_plugin_test_channel'
SERVICE_NAME = 'testservice'
CHANNEL_ID = ObjectId("556721a52a2e7febd2744307")
TEST_DATA_AFTER = [
    [37.61556,  55.75222],
    [34.37167,  53.25209],
    [49.66007,  58.59665],
    [34.34691,  61.78491],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [30.31413,  59.93863]
]
OLD_GEONAMES_LOGIN = getGeonamesLogin()
NEW_GEONAMES_LOGIN = r'geo2tag'
config = RawConfigParser()
config.read(r'../../config/config.ini')
db = getDbObject(SERVICE_NAME)
points = db['points']


class TestGeocoderImportBackFunc(TestCase):
    def setUp(self):
        config['geocoding']['geonames_login'] = NEW_GEONAMES_LOGIN
        with open(r'../config.ini', 'wb') as configfile:
            config.write(configfile)
        self.data_before = list(points.find({'channel_id': CHANNEL_ID}))
        self.addresses_before = [point['location']['coordinates'] for point in self.data_before]

    def tearDown(self):
        config['geocoding']['geonames_login'] = OLD_GEONAMES_LOGIN
        with open(r'../config.ini', 'wb') as configfile:
            config.write(configfile)

    def testGeocoderImportBackFunc(self):
        for point in self.addresses_before:
            self.assertEqual(point, [0, 0])
        geocoderImport(None, CHANNEL_NAME, SERVICE_NAME)
        data_after = list(points.find({'channel_id': CHANNEL_ID}))
        addresses = [point['location']['coordinates'] for point in data_after]
        for i in range(len(TEST_DATA_AFTER)):
            self.assertEqual(addresses[i], TEST_DATA_AFTER[i])
