import inspect
import re
from unittest import TestCase
from open_karelia_objects_parser import OpenKareliaObjectsParser
from open_data_objects_parser import OpenDataObjectsParser

INHERITANCE_OK_PATT = re.compile(
    "<class 'open_karelia_objects_parser.OpenKareliaObjectsParser'.*"
    "class 'open_data_objects_parser.OpenDataObjectsParser'.*>")


class testODOL(OpenDataObjectsParser):
    pass


class testODOLimpl(OpenDataObjectsParser):

    def parse(self):
        return self.data


class TestOKObjetcsParserRefactoring(TestCase):

    def testOKObjetcsLoaderRefactoring_inheritance(self):
        self.assertIsNotNone(
            re.search(
                INHERITANCE_OK_PATT, unicode(
                    inspect.getmro(OpenKareliaObjectsParser))))

    def testOKObjetcsLoaderRefactoring_notInmlementedException(self):
        with self.assertRaises(TypeError):
            testODOL('test')

    def testOKObjetcsLoaderRefactoring_inmlementedException(self):
        self.assertEqual(testODOLimpl('test').parse(), 'test')
