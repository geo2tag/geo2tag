from unittest import TestCase
from flask import request
from flask import Flask
from werkzeug.exceptions import BadRequest
from json import dumps
import sys
sys.path.append('../plugins/ok_import')
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
        threadJobObj = ThreadJob(
            backgroundFunction,
            channelName,
            openDataUrl,
            showObjectUrl,
            showImageUrl,
            serviceName)
        threadJobObj.start()
        time1 = threadJobObj.describe().get('time')
        threadJobObj.thread.join(1.0)
        time2 = threadJobObj.describe().get('time')
        self.assertEquals(time1, time2)
