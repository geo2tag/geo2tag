import unittest
import sys
import os
sys.path.append('../')
from main import initApp
from plugins import getPluginList
class TestGt1417(unittest.TestCase):
    def testGt1417(self):
        os.chdir('..')
        initApp()
        os.chdir('../..')
        from main import api
        resources = api.endpoints
        self.assertTrue('resource_gt_1416' in resources)
        self.assertTrue('resource_gt_1417' in resources)
        os.chdir('tst')
