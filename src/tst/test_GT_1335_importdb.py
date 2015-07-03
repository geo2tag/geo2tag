from unittest import TestCase
from pymongo import MongoClient
import os

import sys
sys.path.append('../')
import config_reader
sys.path.append('../../scripts/db/')
os.system('python setupMasterDbTemplate.py')

db = MongoClient(config_reader.getHost(), config_reader.getPort())[config_reader.getDbName()]
MYCOLLECTION = 'testdump_forimport'
COUNT = 1
class TestImportDb(TestCase):
    def testMyImport(self):
        count_mycoll = db[MYCOLLECTION].count()
        self.assertEqual(count_mycoll, COUNT)