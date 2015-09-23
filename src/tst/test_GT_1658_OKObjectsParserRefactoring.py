import inspect
import json
import re
from unittest import TestCase
import sys
sys.path.append('../plugins/ok_import/')
from open_karelia_objects_parser import OpenKareliaObjectsParser
sys.path.append('../open_data_import/')
from open_data_objects_parser import OpenDataObjectsParser

INHERITANCE_OK_PATT = re.compile('<class open_karelia_objects_parser.OpenKareliaObjectsParser.*'
                                 'class open_data_objects_parser.OpenDataObjectsParser.*>')
class testODOL(OpenDataObjectsParser):
    pass
test_class = testODOL('test')


class TestOKObjetcsLoaderRefactoring(TestCase):
    def testOKObjetcsLoaderRefactoring_inheritance(self):
        self.assertNotEqual(re.search(INHERITANCE_OK_PATT, str(inspect.getmro(OpenKareliaObjectsParser))), None)

    def testOKObjetcsLoaderRefactoring_notInmlementedException(self):
        with self.assertRaises(NotImplementedError):
            test_class.parse()