# -*- coding: utf-8 -*-
from basic_selenium_test import BasicSeleniumTest


TEST_URL = '/instance/admin/plugin/config/plugin_for_test_config'
VALID_CONFIG = u'[SECTION1]\nopt11=val11\n' + \
    '[SECTION2]\nopt21=val21\nopt22=val22\nopt23=val23'
TEST_TEXTAREA_ID = 'container_config_plugin'
TEST_SCRIPT_RETURN_VALUE = 'return $("#' + TEST_TEXTAREA_ID + '").val()'


class TestConfigPlugin(BasicSeleniumTest):

    def testConfigPluginOpen(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        result = self.driver.execute_script(TEST_SCRIPT_RETURN_VALUE)
        print result
        self.assertEqual(result, VALID_CONFIG)
