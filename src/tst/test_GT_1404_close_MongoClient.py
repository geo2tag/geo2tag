#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from db_model import closeConnection, getClientObject
getClientObject()
from db_model import MONGO_CLIENT
class test_GT_1404Close_MongoClient(TestCase):
    def test_Close_MongoClient(self):        
        self.assertEquals(MONGO_CLIENT.is_primary, True)
        closeConnection() 
        self.assertEquals(MONGO_CLIENT.is_primary, False) 