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

METHOD = 'POST'
DATA_ARR = ['channelName', 'openDataUrl', 'showObjectUrl', 'showImageUrl']
TEST_VAL_PREFIX = 'test_val_'
DATA = {
    DATA_ARR[0]: TEST_VAL_PREFIX + DATA_ARR[0],
    DATA_ARR[1]: TEST_VAL_PREFIX + DATA_ARR[1],
    DATA_ARR[2]: TEST_VAL_PREFIX + DATA_ARR[2],
    DATA_ARR[3]: TEST_VAL_PREFIX + DATA_ARR[3]
}
INCORRECT_DATA = {
    DATA_ARR[0]: 123456,
    DATA_ARR[1]: TEST_VAL_PREFIX + DATA_ARR[1],
    DATA_ARR[3]: 123456
}


class TestOKImportParserPost(TestCase):

    def testOKImportParserPostDone(self):
        with app.test_request_context(data=dumps({"channelName":"test_GT_1286","openDataUrl":"http://mobile.openkarelia.org//get_nearest_objects?latitude=61.787458487564&longitude=34.362810647964", "showObjectUrl":"", "showImageUrl":""}), method=METHOD):
            job1 = JobManager.getJobs()
            job2 = JobManager.getJobs()
            self.assertEquals(job1[0].get('time'), job2[0].get('time'))