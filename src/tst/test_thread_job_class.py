#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from db_model import getDbObject
from thread_job import ThreadJob
import datetime
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
    self.stop()
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
        threadJobObj.internalStart()
        threadJobObj.stop()
        statistic = threadJobObj.getTimeStatistics()
        self.assertEquals(type(statistic), type(datetime.timedelta()))
        describe = threadJobObj.describe()
        self.assertEquals(len(describe.get('_id')), 12)
        self.assertEquals(len(describe.get('time')), 14)
        self.assertEquals(describe.get('done'), True)
        self.assertEquals(describe.get('channelName'), channelName)
        self.assertEquals(describe.get('openDataUrl'), openDataUrl)
        self.assertEquals(describe[IMPORTDATADICT].get('showImageUrl'), showImageUrl)
        self.assertEquals(describe[IMPORTDATADICT].get('showObjectUrl'), showObjectUrl)
        self.assertEquals(describe.get('serviceName'), serviceName)
        self.assertEquals(threadJobObj.channelName, channelName)
        self.assertEquals(threadJobObj.openDataUrl, openDataUrl)
        self.assertEquals(threadJobObj.importDataDict.get('showImageUrl'), showImageUrl)
        self.assertEquals(threadJobObj.importDataDict.get('showObjectUrl'), showObjectUrl)
        self.assertEquals(threadJobObj.serviceName, serviceName)
