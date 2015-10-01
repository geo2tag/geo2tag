from unittest import TestCase
import sys
sys.path.append('../plugins/ok_import/')
from ok_import_resource_parser import OKImportParser
sys.path.append('../open_data_import/')
from od_import_parser import OdImportParser


class TestRefactoringOkImportResourceParser(TestCase):

    def testOkImportParser_inheritance(self):
        self.assertTrue( issubclass(OKImportParser, OdImportParser) )

    def testFields(self):
        self.assertEqual(len(OKImportParser.mandatoryFields), 4)
        self.assertEqual(len(OdImportParser.mandatoryFields), 2)    
