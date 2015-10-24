from unittest import TestCase
from ok_import_resource_parser import OKImportParser
from od_import_parser import OdImportParser


class TestRefactoringOkImportResourceParser(TestCase):

    def testOkImportParser_inheritance(self):
        self.assertTrue(issubclass(OKImportParser, OdImportParser))

    def testFields(self):
        self.assertEqual(len(OKImportParser.mandatoryFields), 4)
        self.assertEqual(len(OdImportParser.mandatoryFields), 2)
