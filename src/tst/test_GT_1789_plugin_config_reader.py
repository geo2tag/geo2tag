import unittest
from plugin_config_reader import PluginConfigReader
import os

TEST_CONTENT = {
    u'test_2': {
        u'test_21': u'test_21',
        u'test_22': u'test_22'},
    u'test_4': {
        u'test_41': u'test_41',
        u'test_42': u'test_42'}}

TEST_RESULT = {
    u'test_1': {
        u'test_1': u'test_1'},
    u'test_3': {
        u'test_31': u'test_31',
        u'test_32': u'test_32',
        u'test_33': u'test_33'},
    u'test_4': {
        u'test_41': u'test_42'}}

TEST_RESULT_2 = {
    u'test_4': {
        u'test_41': u'test_41',
        u'test_42': u'test_42'},
    u'test_3': {
        u'test_31': u'test_31',
        u'test_33': u'test_33',
        u'test_32': u'test_32'},
    u'test_2': {
        u'test_21': u'test_21',
        u'test_22': u'test_22'},
    u'test_1': {
        u'test_1': u'test_1'}}
TEST_NAME = 'test_catalog_for_config'


class TestPluginConfigReader(unittest.TestCase):

    def testPluginConfigReader(self):
        pluginConfigReader = PluginConfigReader(TEST_NAME)
        PATH = pluginConfigReader.file_path
        os.remove(PATH)
        open(TEST_NAME, 'w')
        pluginConfigReader = PluginConfigReader(TEST_NAME)
        pluginConfigReader.setConfigContent(TEST_RESULT)
        conf = pluginConfigReader.getConfigContent()
        self.assertEquals(conf, TEST_RESULT)
        pluginConfigReader.setConfigContent(TEST_CONTENT)
        conf = pluginConfigReader.getConfigContent()
        self.assertEquals(conf, TEST_RESULT_2)
