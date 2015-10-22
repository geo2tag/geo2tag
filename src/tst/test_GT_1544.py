from unittest import TestCase
from flask import Flask
from thread_job import ThreadJob
from time import sleep
app = Flask(__name__)

TEST_channelName = 'channelName'
TEST_openDataUrl = 'openDataUrl'
TEST_showImageUrl = 'showImageUrl'
TEST_showObjectUrl = 'showObjectUrl'
TEST_serviceName = 'serviceName'


def backgroundFunction(
        self,
        channelName=TEST_channelName,
        openDataUrl=TEST_openDataUrl,
        showObjectUrl=TEST_showObjectUrl,
        showImageUrl=TEST_showImageUrl,
        serviceName=TEST_serviceName):
    self.stop()
    print channelName, openDataUrl, showObjectUrl, showImageUrl, showImageUrl, \
        serviceName
    return []


class Test_GT_1544(TestCase):

    def test_GT_1544(self):
        importDataDict = {
            TEST_showImageUrl: TEST_showImageUrl,
            TEST_showObjectUrl: TEST_showObjectUrl}
        threadJobObj = ThreadJob(
            backgroundFunction,
            TEST_channelName,
            TEST_openDataUrl,
            importDataDict,
            TEST_serviceName)
        threadJobObj.start()
        while not threadJobObj.done:
            sleep(0.1)
        time1 = threadJobObj.describe().get('time')
        sleep(0.05)
        time2 = threadJobObj.describe().get('time')
        self.assertEquals(time1, time2)
