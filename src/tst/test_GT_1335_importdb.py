from db_model import getDbObject
from unittest import TestCase
import os
import config_reader

TEST_PATH = os.getcwd()
DB_TAG = '--dbName '
CONF_TAG = '--config '
CONFIG_NAME = 'config/config.ini'
TEST_DB = 'master_db_template'
PATH_DB = 'python scripts/db/setupMasterDbTemplate.py ' + DB_TAG + TEST_DB
PATH_CONF = \
    'python scripts/db/setupMasterDbTemplate.py ' + CONF_TAG + CONFIG_NAME
MYCOLLECTION = 'testdump_forimport'
COUNT = 1


class TestImportDb(TestCase):

    def setUp(self):
        os.chdir('../../')
        os.system('./scripts/db/drop_test_db.sh')
        self.db = getDbObject(TEST_DB)

    def tearDown(self):
        os.system('./scripts/db/import_test_db.sh')
        os.chdir(TEST_PATH)

    def testMyImport_Db_Tag(self):
        os.system(PATH_DB)
        count_mycoll = self.db[MYCOLLECTION].count()
        self.assertEqual(count_mycoll, COUNT)

    def testMyImport_Conf_Tag(self):
        os.system(PATH_CONF)
        count_mycoll = self.db[MYCOLLECTION].count()
        self.assertEqual(count_mycoll, COUNT)
