#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

"""import sys
import os
sys.path.append('../')
sys.path.append('../plugins/ok_import/')"""

from db_model import getDbObject
from thread_job import ThreadJob
import datetime
from time import sleep
channelName = 'channelName'
openDataUrl = 'openDataUrl'
showImageUrl = 'showImageUrl'
showObjectUrl = 'showObjectUrl'
serviceName = 'serviceName'
IMPORTDATADICT = 'importDataDict'


def backgroundFunction(
        self,
        channelName=channelName,
        openDataUrl=openDataUrl,
        showObjectUrl=showObjectUrl,
        showImageUrl=showImageUrl,
        serviceName=serviceName):
    print 'I\'m a thread'
    return [channelName, openDataUrl, showImageUrl, showImageUrl, serviceName]


class Test_GT_1506_class_thread_job(TestCase):

    def test_GT_1506_class_thread_job(self):
        importDataDict_val = {showImageUrl:showImageUrl,showObjectUrl:showObjectUrl}
        threadJobObj = ThreadJob(
            backgroundFunction,
            channelName,
            openDataUrl,
            importDataDict_val,
            serviceName)
        threadJobObj.start()
        self.assertTrue(threadJobObj.thread.is_alive())
        threadJobObj.stop()
        if threadJobObj.thread.is_alive():
            while not threadJobObj.thread.is_alive():
                sleep(0.1)
        self.assertFalse(threadJobObj.thread.is_alive())
        self.assertTrue(threadJobObj.done)
        statistic = threadJobObj.getTimeStatistics()
        self.assertEquals(type(statistic), type(datetime.timedelta()))
        describe = threadJobObj.describe()
        self.assertEquals(len(describe.get('_id')), 12)
        self.assertEquals(len(describe.get('time')), 14)
        self.assertEquals(describe.get('done'), True)
        self.assertEquals(describe.get('channelName'), channelName)
        self.assertEquals(describe.get('openDataUrl'), openDataUrl)
        self.assertEquals(describe.get('showImageUrl'), showImageUrl)
        self.assertEquals(describe.get('showObjectUrl'), showObjectUrl)
        self.assertEquals(describe.get('serviceName'), serviceName)
        self.assertEquals(threadJobObj.channelName, channelName)
        self.assertEquals(threadJobObj.openDataUrl, openDataUrl)
        self.assertEquals(threadJobObj.importDataDict.get('showImageUrl'), showImageUrl)
        self.assertEquals(threadJobObj.importDataDict.get('showObjectUrl'), showObjectUrl)
        self.assertEquals(threadJobObj.serviceName, serviceName)
