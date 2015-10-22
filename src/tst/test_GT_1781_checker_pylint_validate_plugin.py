from unittest import TestCase
import os
import sys
import shutil

GOOD_NAME_PLUGIN = 'test_plugin'
FAIL_NAME_PLUGIN_1 = 'test_plugin_for_fail'
FAIL_NAME_PLUGIN_2 = 'test_plugin_for_load_fail_gt_1435'
PY_SCRIPT = 'python ./scripts/validate_plugin.py '
RES_GOOD_PLUGIN = 'Error code: 0\n'
RES_FAIL_1_PLUGIN = 'No required function getPluginResources\n\n\
Error code: 1\n'
RES_FAIL_2_PLUGIN = '======= Module: src.plugins.test_plugin_for_\
load_fail_gt_1435.main =======\nNo required function getPluginResources\n\
No required function getPluginInfo\n\nError code: 1\n'


class TestValidatePlugin_PYLINT(TestCase):

    def testValidatePlugin_GOOD(self):
        os.chdir('../..')
        data = os.popen(PY_SCRIPT + GOOD_NAME_PLUGIN).read()
        self.assertEqual(RES_GOOD_PLUGIN, data)
        os.chdir('src/tst')

    def testValidatePlugin_FAIL_1(self):
        os.chdir('../..')
        data = os.popen(PY_SCRIPT + FAIL_NAME_PLUGIN_1).read()
        self.assertEqual(RES_FAIL_1_PLUGIN, data)
        os.chdir('src/tst')

    def testValidatePlugin_FAIL_2(self):
        os.chdir('../..')
        data = os.popen(PY_SCRIPT + FAIL_NAME_PLUGIN_2).read()
        self.assertEqual(RES_FAIL_2_PLUGIN, data)
        os.chdir('src/tst')
