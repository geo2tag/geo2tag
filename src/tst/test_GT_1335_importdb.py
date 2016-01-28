from unittest import TestCase
import os
import config_reader

TEST_PATH = os.getcwd()


class TestImportDb(TestCase):

    def setUp(self):
        os.chdir('../../')
        os.system('./scripts/db/drop_test_db.sh')

    def tearDown(self):
        os.system('./scripts/db/import_test_db.sh')
        os.chdir(TEST_PATH)

    def testMyImport_Db_Tag(self):
        pass
