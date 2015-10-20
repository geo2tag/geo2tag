#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from thread_job import ThreadJob
import datetime
from time import sleep

TEST_channelName = 'channelName'
TEST_openDataUrl = 'openDataUrl'
TEST_showImageUrl = 'showImageUrl'
TEST_showObjectUrl = 'showObjectUrl'
TEST_serviceName = 'serviceName'
IMPORTDATADICT = 'importDataDict'


def backgroundFunction(
        self,
        channelName=TEST_channelName,
        openDataUrl=TEST_openDataUrl,
        showObjectUrl=TEST_showObjectUrl,
        showImageUrl=TEST_showImageUrl,
        serviceName=TEST_serviceName):
    print self, channelName, openDataUrl, showObjectUrl, showImageUrl, serviceName
    sleep(2)
    return None


class Test_GT_1506_class_thread_job(TestCase):

    def test_GT_1506_class_thread_job(self):
        importDataDict_val = {
            TEST_showImageUrl: TEST_showImageUrl,
            TEST_showObjectUrl: TEST_showObjectUrl}
        threadJobObj = ThreadJob(
            backgroundFunction,
            TEST_channelName,
            TEST_openDataUrl,
            importDataDict_val,
            TEST_serviceName)
        threadJobObj.start()
        self.assertTrue(threadJobObj.thread.is_alive())
        threadJobObj.stop()
        while threadJobObj.thread.is_alive() is True:
            sleep(0.1)
        self.assertFalse(threadJobObj.thread.is_alive())
        self.assertTrue(threadJobObj.done)
        statistic = threadJobObj.getTimeStatistics()
        self.assertEquals(type(statistic), type(datetime.timedelta()))
        describe = threadJobObj.describe()
        self.assertEquals(len(describe.get('_id')), 12)
        self.assertEquals(len(describe.get('time')), 14)
        self.assertEquals(describe.get('done'), True)
        self.assertEquals(describe.get('channelName'), TEST_channelName)
        self.assertEquals(describe.get('openDataUrl'), TEST_openDataUrl)
        self.assertEquals(describe.get('showImageUrl'), TEST_showImageUrl)
        self.assertEquals(describe.get('showObjectUrl'), TEST_showObjectUrl)
        self.assertEquals(describe.get('serviceName'), TEST_serviceName)
        self.assertEquals(threadJobObj.channelName, TEST_channelName)
        self.assertEquals(threadJobObj.openDataUrl, TEST_openDataUrl)
        self.assertEquals(
            threadJobObj.importDataDict.get('showImageUrl'),
            TEST_showImageUrl)
        self.assertEquals(
            threadJobObj.importDataDict.get('showObjectUrl'),
            TEST_showObjectUrl)
        self.assertEquals(threadJobObj.serviceName, TEST_serviceName)
