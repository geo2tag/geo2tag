#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from datetime import datetime
from pymongo import MongoClient

import sys
sys.path.append('../')

from config_reader import getHost, getPort, getDbName
from db_model import updateService

SERVICES = "services"
TEST = "test"
TEST_SERVICE = "testservice_"
CONFIG = "config"
LOG_SIZE = "log_size"
LOG_PATH = "log_path"
LOG_DATE = "log_date"

NOT_TESTED_LOG_SIZE = 0
NOT_TESTED_LOG_PATH = "not_tested"

DATE_TODAY = datetime(2015,1,1)

testConfigDictForPathAndSize = {LOG_PATH : TEST, LOG_SIZE : 100}
testConfigDictForPath = {LOG_PATH : TEST}
testConfigDictForSize = {LOG_SIZE : 100}
testConfigDictForNoChanges = {}
testConfigDictForPathAndSizeAndDate = {LOG_PATH : TEST, LOG_SIZE : 100, LOG_DATE : DATE_TODAY}

db = MongoClient(getHost(), getPort())[getDbName()]
services_collection = db[SERVICES]

def prepareDb() :
	"making unique services"
	services_collection.remove()
	for i in range(100) :
		services_collection.insert({
			"config" : { LOG_PATH : NOT_TESTED_LOG_PATH, LOG_SIZE : NOT_TESTED_LOG_SIZE }, 
			"name" : (TEST_SERVICE + str(i)), 
			"owner_id" : "" 
		})

def prepareDbRemoveSubDoc() :
	"removing sub-document called 'config' from service called 'testservice_1'"
	services_collection.update(
		{"name" : TEST_SERVICE + "1"},
		{"$unset" : {CONFIG : ""}},
		multi = True
	)

class TestUpdateService(TestCase) :
	def testUpdateServiceWithoutConfigSubDocuments(self) :
		prepareDb()
		prepareDbRemoveSubDoc()
		#checking if in sub-document of service called 'testservice_1' field 'config' doesn't exist
		#and creating 'config' with 'path' and 'size' in it
		changed_service = None
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForPathAndSize) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_PATH], testConfigDictForPathAndSize[LOG_PATH])
		self.assertEqual(changed_service[CONFIG][LOG_SIZE], testConfigDictForPathAndSize[LOG_SIZE])

		prepareDb()
		prepareDbRemoveSubDoc()
		#checking if in sub-document of service called 'testservice_1' field 'config' doesn't exist
		#and creating 'config' with only 'path' in it
		changed_service = None
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForPath) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_PATH], testConfigDictForPath[LOG_PATH])
		self.assertTrue(LOG_SIZE not in changed_service[CONFIG])

		prepareDb()
		prepareDbRemoveSubDoc()
		#checking if in sub-document of service called 'testservice_1' field 'config' doesn't exist
		#and creating 'config' with only 'size' in it
		changed_service = None
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForSize) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_SIZE], testConfigDictForSize[LOG_SIZE])
		self.assertTrue(LOG_PATH not in changed_service[CONFIG])

		prepareDb()
		prepareDbRemoveSubDoc()
		#checking if in sub-document of service called 'testservice_1' field 'config' doesn't exist
		#and creating 'config' with only 'size' in it but it's not going to happend, dict to get changes is empty
		changed_service = None
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForNoChanges) :
			changed_service = doc
		self.assertTrue(CONFIG not in changed_service)

		prepareDb()
		prepareDbRemoveSubDoc()
		#checking if in sub-document of service called 'testservice_1' field 'config' doesn't exist
		#and creating 'config' with 'path' and 'size' in it
		changed_service = None
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForPathAndSizeAndDate) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_PATH], testConfigDictForPathAndSizeAndDate[LOG_PATH])
		self.assertEqual(changed_service[CONFIG][LOG_SIZE], testConfigDictForPathAndSizeAndDate[LOG_SIZE])
		self.assertEqual(changed_service[CONFIG][LOG_DATE], testConfigDictForPathAndSizeAndDate[LOG_DATE])


	def testUpdateServiceWithinConfigSubDocuments(self) :
		prepareDb()
		changed_service = None
		#considering that every service is unique
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForPathAndSize) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_PATH], testConfigDictForPathAndSize[LOG_PATH])
		self.assertEqual(changed_service[CONFIG][LOG_SIZE], testConfigDictForPathAndSize[LOG_SIZE])

		prepareDb()
		changed_service = None
		#considering that every service is unique
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForPath) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_PATH], testConfigDictForPath[LOG_PATH])
		self.assertEqual(changed_service[CONFIG][LOG_SIZE],NOT_TESTED_LOG_SIZE)

		prepareDb()
		changed_service = None
		#considering that every service is unique
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForSize) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_SIZE], testConfigDictForSize[LOG_SIZE])
		self.assertEqual(changed_service[CONFIG][LOG_PATH],NOT_TESTED_LOG_PATH)

		prepareDb()
		changed_service = None
		#considering that every service is unique
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForNoChanges) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_PATH],NOT_TESTED_LOG_PATH)
		self.assertEqual(changed_service[CONFIG][LOG_SIZE],NOT_TESTED_LOG_SIZE)

		prepareDb()
		changed_service = None
		#considering that every service is unique
		for doc in updateService(TEST_SERVICE  + "1", testConfigDictForPathAndSizeAndDate) :
			changed_service = doc
		self.assertTrue(CONFIG in changed_service)
		self.assertEqual(changed_service[CONFIG][LOG_PATH], testConfigDictForPathAndSizeAndDate[LOG_PATH])
		self.assertEqual(changed_service[CONFIG][LOG_SIZE], testConfigDictForPathAndSizeAndDate[LOG_SIZE])
		self.assertEqual(changed_service[CONFIG][LOG_DATE], testConfigDictForPathAndSizeAndDate[LOG_DATE])