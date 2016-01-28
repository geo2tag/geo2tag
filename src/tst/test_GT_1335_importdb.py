from db_model import getDbObject
from unittest import TestCase
import os

TEST_PATH = os.getcwd()
DB_TAG = '--dbName '
CONF_TAG = '--config '
CONFIG_NAME = 'config/test_config.ini'
TEST_DB = 'master_db_template'
PATH_DB = 'python scripts/db/setupMasterDbTemplate.py ' + DB_TAG + TEST_DB
PATH_CONF = \
    'python scripts/db/setupMasterDbTemplate.py ' + CONF_TAG + CONFIG_NAME
COLLECTION_MASTER = 'testdump_forimport'
COUNT_0 = 0


class TestImportDb(TestCase):

    def setUp(self):
        os.chdir('../../')
        self.db_master = getDbObject(TEST_DB)

    def tearDown(self):
        os.chdir(TEST_PATH)

    def testMyImport_Db_Tag(self):
        os.system(PATH_DB)
        count_mycoll = self.db_master[COLLECTION_MASTER].count()
        self.assertNotEqual(count_mycoll, COUNT_0)

    def testMyImport_Conf_Tag(self):
        os.system(PATH_CONF)
        count_mycoll = self.db_master[COLLECTION_MASTER].count()
        self.assertNotEqual(count_mycoll, COUNT_0)
