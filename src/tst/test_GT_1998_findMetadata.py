#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from db_model import findMetadata
from bson.objectid import ObjectId 


class TestFindMetadata(TestCase):

    def testMetadata(self):
        TEST_QUERY = {'dict.dict2.0':1}
        TEST_NUMBER = 1
        TEST_OFFSET = 0
        VALID_LENGTH = 1
        VALID_ID = ObjectId('552833515404411781370723') 

        result = findMetadata(TEST_SERVICE, TEST_QUERY, \
                              TEST_NUMBER, TEST_OFFSET)
        self.assertEquals(len(result), VALID_LENGTH)
        self.assertEquals(result[0]['_id'],VALID_ID)
