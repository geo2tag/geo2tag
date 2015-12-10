#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from db_model import findMetadata
from bson.objectid import ObjectId


class TestFindMetadata(TestCase):

    def testMetadata(self):
        TEST_QUERY = {'json.dict.dict2.0': 1}
        TEST_NUMBER = 1
        TEST_OFFSET = 0
        TEST_SERVICE = 'testservice'
        VALID_LENGTH = 1
        VALID_ID = ObjectId('552833515404411781370723')

        result = findMetadata(TEST_SERVICE, TEST_NUMBER,
                              TEST_OFFSET, TEST_QUERY)
        result = list(result)
        self.assertEquals(len(result), VALID_LENGTH)
        self.assertEquals(result[0]['_id'], VALID_ID)
