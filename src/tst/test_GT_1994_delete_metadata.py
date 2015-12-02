#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from db_model import deletePointById, getDbObject
from metadata_does_not_exist_exception import MetadataDoesNotExistException

TEST_DB = "testservice"
TEST_COLLECTION = "metadata"
ID = "_id"


class TestDeletePointById(unittest.TestCase):

    def testDeletePointById(self):
        collection = getDbObject(TEST_DB)[TEST_COLLECTION]
        db = getDbObject(DB)
        obj_id = db[COLLECTION].save({NAME: 'test_GT_1306'})
        with self.assertRaises(PointDoesNotExist):
            deletePointById('testservice', '111111111111111111111111')
        deletePointById('testservice', obj_id)
        obj = db[COLLECTION].find_one({ID: obj_id})
        self.assertEqual(obj, None)
