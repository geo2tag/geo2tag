#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from datetime import datetime, date, time
from config_reader import getHost, getPort, getDbName
from db_model import getLog, getDbObject

DB = "geomongo"
WRONG_DB = "wrong_db"
COLLECTION = "log"

DATE_TO = datetime(2100, 1, 1)
DATE_FROM = datetime(2000, 1, 1)
WRONG_DATE_TO = datetime(3500, 1, 1)
WRONG_DATE_FROM = datetime(3000, 1, 1)


def prepareDb():
    # Connecting to db 'geomongo', collection 'log'
    db = getDbObject()
    collection = db[COLLECTION]
    for i in range(100):
        # Inserting new post with date
        post = {"user_id": "stub",
                "date": datetime((2000 + i), 1, 1).utcnow().replace(2000 + i),
                "message": "test",
                "service": "testservice"}
        collection.insert(post)


class TestGetLog(TestCase):

    def testForDates(self):
        print "Test for dates"
        prepareDb()
        # Test when dateFrom and dateTo vars are equal to None
        self.assertEqual(getLog(DB, None, None, None, None), [])
        # Test when dateTo is equal to None
        log = getLog(DB, None, None, DATE_FROM, None)
        self.assertTrue(log.count(True) > 0)
        # Test when dateFrom is equal to None
        log = getLog(DB, None, None, None, DATE_TO)
        self.assertTrue(log.count(True) > 0)
        # Test when dateTo is lower than dateFrom
        self.assertEqual(getLog(DB, None, None, WRONG_DATE_FROM, DATE_TO), [])
        # Test when dateTo and dateFrom are normal
        log = getLog(DB, None, None, DATE_FROM, DATE_TO)
        self.assertTrue(log.count(True) > 0)
        # Test when dateTo and dateFrom are normal
        log = getLog(DB, None, None, WRONG_DATE_FROM, WRONG_DATE_TO)
        self.assertTrue(log.count(True) == 0)
