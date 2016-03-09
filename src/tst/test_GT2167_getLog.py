#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from datetime import datetime
from db_model import getLog, getDbObject

DB = "geomongo"
WRONG_DB = "wrong_db"
COLLECTION = "log"

DATE_TO = datetime(2100, 1, 1)
DATE_FROM = datetime(2000, 1, 1)
WRONG_DATE_TO = datetime(3500, 1, 1)
WRONG_DATE_FROM = datetime(3000, 1, 1)
MESSAGE = 'testGT_2167'
db = getDbObject()
collection = db[COLLECTION]


def prepareDb():
    for i in range(10):
        # Inserting new post with date
        post = {"user_id": "stub",
                "date": datetime((2000 + i), 1, 1).utcnow().replace(2000 + i),
                "message": "testGT_2167",
                "service": "testservice"}
        collection.insert(post)


def tearDown(self):
    collection.remove(
        {"message": MESSAGE})


class TestGetLog(TestCase):

    def testForDates(self):
        prepareDb()
        logList = list(getLog(DB, 10, None, None, None))
        for i in range(len(logList) - 1):
            self.assertTrue(logList[i]['date'] > logList[i + 1]['date'])
        logList = list(getLog(DB, 10, None, DATE_FROM, DATE_TO))
        for i in range(len(logList) - 1):
            self.assertTrue(logList[i]['date'] > logList[i + 1]['date'])
        logList = list(getLog(DB, 10, None, DATE_FROM, None))
        for i in range(len(logList) - 1):
            self.assertTrue(logList[i]['date'] > logList[i + 1]['date'])
        logList = list(getLog(DB, 10, None, None, DATE_TO))
        for i in range(len(logList) - 1):
            self.assertTrue(logList[i]['date'] > logList[i + 1]['date'])
