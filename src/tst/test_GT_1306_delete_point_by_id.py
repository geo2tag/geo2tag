#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from db_model import deletePointById, getDbObject
from point_does_not_exist import PointDoesNotExist

DB = "testservice"
COLLECTION = "points"
ID = "_id"
NAME = 'name'


class TestDeletePointById(unittest.TestCase):

    def testDeletePointById(self):
        db = getDbObject(DB)
        obj_id = db[COLLECTION].save({NAME: 'test_GT_1306'})
        with self.assertRaises(PointDoesNotExist):
            deletePointById('testservice', '111111111111111111111111')
        deletePointById('testservice', obj_id)
        obj = db[COLLECTION].find_one({ID: obj_id})
        self.assertEqual(obj, None)
