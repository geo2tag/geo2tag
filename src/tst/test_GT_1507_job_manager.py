#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from thread_job import ThreadJob
from job_manager import JobManager

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
    print showObjectUrl
    return [channelName, openDataUrl, showImageUrl, showImageUrl, serviceName]


class Test_GT_1507_class_job_manager(TestCase):

    def test_GT_1507_class_job_manager(self):
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
        manager = JobManager()
        jobId = manager.startJob(threadJobObj)
        self.assertEquals(len(jobId), 12)
        self.assertEquals(type(manager.getJob(jobId)), dict)
        manager.stopJob(jobId)
        self.assertEquals(threadJobObj.done, True)
        self.assertEquals(type(manager.getJobs()), list)
        threadJobObj.stop()
