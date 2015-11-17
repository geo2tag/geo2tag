from unittest import TestCase
from pymongo import MongoClient
import os
import config_reader

TEST_DB = 'master_db_template'
DB_TAG = '--dbName '
CONF_TAG = '--config '
CONFIG_NAME = 'config'
PATH_DB = 'python scripts/db/setupMasterDbTemplate.py ' +  DB_TAG +  TEST_DB
PATH_CONF = 'python scripts/db/setupMasterDbTemplate.py ' +  CONF_TAG +  CONFIG_NAME
TEST_PATH = os.getcwd()

os.chdir('../../')
os.system(PATH_CONF)
os.chdir(TEST_PATH)

db = MongoClient(config_reader.getHost(), config_reader.getPort())[TEST_DB]
MYCOLLECTION = 'testdump_forimport'
COUNT = 1


class TestImportDb(TestCase):

    def testMyImport_Db_Tag(self):
    	os.chdir('../../')
    	os.system('./scripts/db/drop_test_db.sh')
        os.system(PATH_DB)
        count_mycoll = db[MYCOLLECTION].count()
        self.assertEqual(count_mycoll, COUNT)
        os.system('./scripts/db/import_test_db.sh');
        os.chdir(TEST_PATH)

    def testMyImport_Conf_Tag(self):
        count_mycoll = db[MYCOLLECTION].count()
        self.assertEqual(count_mycoll, COUNT)

