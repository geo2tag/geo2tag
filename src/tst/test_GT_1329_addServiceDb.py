#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from db_model import addServiceDb, getDbObject
DB_NAME = 'testservice'
COLLECTION_POINTS_NAME = 'points'


class TestAddServiceDB(TestCase):

    def testAddServiceDB(self):
        db = getDbObject(DB_NAME)
        addServiceDb(DB_NAME)
        indexes = db[COLLECTION_POINTS_NAME].index_information()
        self.assertTrue('location_2dsphere' in indexes.keys())
        self.assertTrue('date_-1' in indexes.keys())
