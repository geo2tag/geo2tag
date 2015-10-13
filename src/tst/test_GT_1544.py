from unittest import TestCase
from flask import request
from flask import Flask
from werkzeug.exceptions import BadRequest
from json import dumps
from ok_import_resource_parser import OKImportParser
from thread_job import ThreadJob
from job_manager import JobManager
import json
from time import sleep
app = Flask(__name__)

channelName = 'channelName'
openDataUrl = 'openDataUrl'
showImageUrl = 'showImageUrl'
showObjectUrl = 'showObjectUrl'
serviceName = 'serviceName'


def backgroundFunction(
        self,
        channelName=channelName,
        openDataUrl=openDataUrl,
        showObjectUrl=showObjectUrl,
        showImageUrl=showImageUrl,
        serviceName=serviceName):
    self.stop()
    return []


class Test_GT_1544(TestCase):

    def test_GT_1544(self):
        importDataDict = {
            showImageUrl: showImageUrl,
            showObjectUrl: showObjectUrl}
        threadJobObj = ThreadJob(
            backgroundFunction,
            channelName,
            openDataUrl,
            importDataDict,
            serviceName)
        threadJobObj.start()
        while not threadJobObj.done:
            sleep(0.1)
        time1 = threadJobObj.describe().get('time')
        sleep(0.05)
        time2 = threadJobObj.describe().get('time')
        self.assertEquals(time1, time2)
