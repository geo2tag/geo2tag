#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
from db_model import getDbObject
sys.path.append('../plugins/ok_import/')
from thread_job import ThreadJob
from job_manager import JobManager
import datetime
channelName = 'channelName'
openDataUrl = 'openDataUrl'
showImageUrl = 'showImageUrl'
showObjectUrl = 'showObjectUrl'
serviceName = 'serviceName'

def backgroundFunction(channelName = channelName, openDataUrl = openDataUrl, showObjectUrl = showObjectUrl, showImageUrl = showImageUrl, serviceName = serviceName):
    return [channelName, openDataUrl, showImageUrl, showImageUrl, serviceName]

class Test_GT_1507_class_job_manager(TestCase):
    def test_GT_1507_class_job_manager(self):
        threadJobObj = ThreadJob(backgroundFunction, channelName, openDataUrl, showObjectUrl, showImageUrl, serviceName)
        threadJobObj.start()
        manager = JobManager()
        jobId = manager.startJob(threadJobObj)
        self.assertEquals(len(jobId), 12)
        self.assertEquals(type(manager.getJob(jobId)), dict)
        manager.stopJob(jobId)
        self.assertEquals(threadJobObj.done, True)
        self.assertEquals(type(manager.getJobs()), list)
        threadJobObj.stop()