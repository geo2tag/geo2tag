#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
import os
from db_model import getDbObject
from thread_job import ThreadJob
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', 'open_data_import/')))
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
        importDataDict = {showImageUrl:showImageUrl,showObjectUrl:showObjectUrl}
        threadJobObj = ThreadJob(
            backgroundFunction,
            channelName,
            openDataUrl,
            importDataDict,
            serviceName)
        self.assertFalse(threadJobObj.done)
        threadJobObj.internalStart()
        self.assertTrue(threadJobObj.done)
