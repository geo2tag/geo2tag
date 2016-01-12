#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from db_model import addServiceDb, getDbObject
DB_NAME = 'testservice'
COLLECTION_POINTS_NAME = 'points'


def checkGeneratedDb(self, dbName):
    db = getDbObject(dbName)
    addServiceDb(dbName)
    indexes = db[COLLECTION_POINTS_NAME].index_information()
    self.assertTrue('location_2dsphere' in indexes.keys())
    self.assertTrue('date_-1' in indexes.keys())
    self.assertTrue('name_1' in indexes.keys())


class TestAddServiceDB(TestCase):

    def testAddServiceDB(self):
        checkGeneratedDb(self, DB_NAME)
