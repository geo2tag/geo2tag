#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
from db_model import getDbObject
sys.path.append('../plugins/ok_import/')
from thread_job_class import ThreadJob
import datetime
channelName = 'channelName'
openDataUrl = 'openDataUrl'
showImageUrl = 'showImageUrl'
showObjectUrl = 'showObjectUrl'
serviceName = 'serviceName'
def backgroundFunction(channelName = channelName, openDataUrl = openDataUrl, showObjectUrl = showObjectUrl, showImageUrl = showImageUrl, serviceName = serviceName):
    return [channelName, openDataUrl, showImageUrl, showImageUrl, serviceName]

class Test_GT_1506_class_thread_job(TestCase):
    def test_GT_1506_class_thread_job(self):
        threadJobObj = ThreadJob(backgroundFunction, channelName, openDataUrl, showObjectUrl, showImageUrl, serviceName)
        threadJobObj.start()
        threadJobObj.internalStart()
        threadJobObj.stop()
        statistic =  threadJobObj.getTimeStatistics()
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
        self.assertEquals(threadJobObj.showImageUrl, showImageUrl)
        self.assertEquals(threadJobObj.showObjectUrl, showObjectUrl)
        self.assertEquals(threadJobObj.serviceName, serviceName)