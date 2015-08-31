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
from time import sleep


def backgroundFunction(
        self,
        channelName=channelName,
        openDataUrl=openDataUrl,
        showObjectUrl=showObjectUrl,
        showImageUrl=showImageUrl,
        serviceName=serviceName):
    self.stop()
    return [channelName, openDataUrl, showImageUrl, showImageUrl, serviceName]


class Test_GT_1558(TestCase):

    def test_GT_1528(self):
        threadJobObj = ThreadJob(
            backgroundFunction,
            channelName,
            openDataUrl,
            showObjectUrl,
            showImageUrl,
            serviceName)
        self.assertFalse(threadJobObj.done)
        threadJobObj.internalStart()
        self.assertTrue(threadJobObj.done)
