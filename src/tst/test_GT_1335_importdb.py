from unittest import TestCase
from pymongo import MongoClient
import os
import sys



sys.path.append('../')
import config_reader

TEST_DB = 'master_db_template'
PATH_SC = '../../scripts/db/'
PATH = 'python ' + PATH_SC + 'setupMasterDbTemplate.py ' + TEST_DB
os.system(PATH)

db = MongoClient(config_reader.getHost(), config_reader.getPort())[TEST_DB]
MYCOLLECTION = 'testdump_forimport'
COUNT = 1

class TestImportDb(TestCase):
    def testMyImport(self):
        count_mycoll = db[MYCOLLECTION].count()
        self.assertEqual(count_mycoll, COUNT)