#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from datetime import datetime
from db_model import getLog, getDbObject

DB = "geomongo"
COLLECTION = "log"
DATE = "date"
USER_ID = "user_id"
STUB = "stub"
MESS = "message"
SERVICE = "service"
TEST_SERVICE = "testservice"
DATE_TO = datetime(2100, 1, 1)
DATE_FROM = datetime(2000, 1, 1)
MESSAGE = 'testGT_2167'
db = getDbObject()
collection = db[COLLECTION]


def prepareDb():
    for i in range(10):
        # Inserting new post with date
        post = {USER_ID: STUB,
                DATE: datetime((2000 + i), 1, 1).utcnow().replace(2000 + i),
                MESS: MESSAGE,
                SERVICE: TEST_SERVICE}
        collection.insert(post)


class TestGetLog(TestCase):

    def tearDown(self):
        collection.remove(
            {MESS: MESSAGE})

    def testForDates(self):
        prepareDb()
        logList = list(getLog(DB, 10, None, None, None))
        for i in range(len(logList) - 1):
            self.assertTrue(logList[i][DATE] > logList[i + 1][DATE])
        logList = list(getLog(DB, 10, None, DATE_FROM, DATE_TO))
        for i in range(len(logList) - 1):
            self.assertTrue(logList[i][DATE] > logList[i + 1][DATE])
        logList = list(getLog(DB, 10, None, DATE_FROM, None))
        for i in range(len(logList) - 1):
            self.assertTrue(logList[i][DATE] > logList[i + 1][DATE])
        logList = list(getLog(DB, 10, None, None, DATE_TO))
        for i in range(len(logList) - 1):
            self.assertTrue(logList[i][DATE] > logList[i + 1][DATE])
