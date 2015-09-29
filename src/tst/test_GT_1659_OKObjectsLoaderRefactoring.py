import inspect
import json
import re
from unittest import TestCase
import sys
sys.path.append('../plugins/ok_import/')
from open_karelia_objects_loader import OpenKareliaObjectsLoader
sys.path.append('../open_data_import/')
from open_data_objects_loader import OpenDataObjectsLoader

INHERITANCE_OK_PATT = re.compile("<class 'open_karelia_objects_loader.OpenKareliaObjectsLoader'.*"
                                 "class 'open_data_objects_loader.OpenDataObjectsLoader'.*>")


class testODOL(OpenDataObjectsLoader):
    pass


class testODOLimpl(OpenDataObjectsLoader):
    def load(self):
        return self.loadUrl


class TestOKObjetcsLoaderRefactoring(TestCase):
    
    def testOKObjetcsLoaderRefactoring_inheritance(self):
        self.assertIsNotNone(re.search(INHERITANCE_OK_PATT, str(inspect.getmro(OpenKareliaObjectsLoader))))

    def testOKObjetcsLoaderRefactoring_notInmlementedException(self):
        with self.assertRaises(TypeError):
            testODOL('test')

    def testOKObjetcsLoaderRefactoring_inmlementedException(self):
        self.assertEqual(testODOLimpl('test').load(), 'test')
