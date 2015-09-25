import unittest
import sys
sys.path.append('../plugins/ok_import/')
sys.path.append('/var/www/geomongo/open_data_import')
from perfom_import_actions import performImportActions
from db_model import getDbObject


class testOdLoaderClass():

    def __init__(self, testOpenDataUrl):
        self.openDataUrl = testOpenDataUrl

    def load(self):
        return "OK"


class testOdParserClass():

    def __init__(self, testOpenData):
        self.openData = testOpenData

    def parse(self):
        return "OK"


class testOdToPointTranslatorClass():

    def __init__(self, testShowImageUrl, testShowObjectUrl,
                 testObject, testVersion, testOpenDataUrl, testChannelId):
        self.showImageUrl = testShowImageUrl
        self.showObjectUrl = testShowObjectUrl
        self.object = testObject
        self.version = testVersion
        self.openDataUrl = testOpenDataUrl
        self.channelId = testChannelId

    def getPoint(self):
        return "OK"


class odToPointsLoaderClass():

    def __init__(self, testServiceName, testPoints):
        self.serviceName = testServiceName
        self.points = testPoints

    def loadPoints(self):
        return "OK"


def callBack(self):
    self.done = True

TEST_SERVICE_NAME = 'testservice'
TEST_CHANNEL_NAME = u'test_channel_1'
TEST_OPEN_DATA_URL = 'test_open_data_url'
TEST_SHOW_OBJECT_URL = 'test_show_object_url'
TEST_SHOW_IMAGE_URL = 'test_show_image_url'


class TestPerfomImportActions(unittest.TestCase):

    def testPerfomImportActions(self):
        performImportActions(
            testOdLoaderClass,
            testOdParserClass,
            testOdToPointTranslatorClass,
            odToPointsLoaderClass,
            TEST_CHANNEL_NAME,
            TEST_OPEN_DATA_URL,
            TEST_SHOW_OBJECT_URL,
            TEST_SHOW_IMAGE_URL,
            TEST_SERVICE_NAME)
