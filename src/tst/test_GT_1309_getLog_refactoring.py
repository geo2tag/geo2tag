#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from datetime import datetime
from db_model import getLog, getDbObject

DATE_TO = datetime(3000, 1, 1)
DATE_FROM = datetime(2100, 1, 1)
DATE_ISERT = datetime(2500, 1, 1)

DB_GEOMONGO = "geomongo"
DB_TESTSERVICE = "testservice"
FAKE_DB = "blablabla"
COLLECTION = "log"
USER_ID = "user_id"
USER_GEOMONGO_ID_VALUE = "GT-1309-geomongo"
USER_TESTSERVICE_ID_VALUE = "GT-1309-testservice"

collection_geomongo = getDbObject(DB_GEOMONGO)[COLLECTION]
collection_testservice = getDbObject(DB_TESTSERVICE)[COLLECTION]


class TestGetLogRefactoring(TestCase):

    def testForGeomongoDb(self):
        collection_geomongo.insert(
            {USER_ID: USER_GEOMONGO_ID_VALUE, "date": DATE_ISERT})
        log_data = list(getLog(DB_GEOMONGO, 0, 0, DATE_FROM, DATE_TO))
        self.assertEqual(log_data[0][USER_ID], USER_GEOMONGO_ID_VALUE)

    def testForTestserviceDb(self):
        collection_testservice.insert(
            {USER_ID: USER_TESTSERVICE_ID_VALUE, "date": DATE_ISERT})
        log_data = list(getLog(DB_TESTSERVICE, 0, 0, DATE_FROM, DATE_TO))
        self.assertEqual(log_data[0][USER_ID], USER_TESTSERVICE_ID_VALUE)

    def testForNoneDb(self):
        self.assertEqual(len(list((getLog(FAKE_DB, 0, 0, DATE_FROM, DATE_TO)))), 0)
