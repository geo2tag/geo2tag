# -*- coding: utf-8 -*-
from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/admin/plugin/config/plugin_for_test_config'
VALID_CONFIG = '[SECTION2]\nopt21=val21\nopt22=val22\nopt23=val23\n' + \
    '[SECTION1]\nopt11=val11\n'
TEST_TEXTAREA_ID = 'container_config_plugin'
TEST_SCRIPT_RETURN_VALUE = 'return $("#' + TEST_TEXTAREA_ID + '").val()'
TEST_TEST_ADD = '[SECTION3]\nopt31=val31\n'
BTN_SAVE_CONFIG = 'save_plugin_btn'
VALID_CONFIG_AFTER_SAVING = '[SECTION3]\nopt31=val31\n' + \
    '[SECTION2]\nopt21=val21\nopt22=val22\nopt23=val23\n' + \
    '[SECTION1]\nopt11=val11\n'
TEST_SCRIPT_CHANGE_VAL = '$("#' + TEST_TEXTAREA_ID + '").val("")'



class TestConfigPlugin(BasicSeleniumTest):

    def testConfigPluginOpen(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        result = self.driver.execute_script(TEST_SCRIPT_RETURN_VALUE)
        self.assertEqual(result, VALID_CONFIG)

    def testConfigPluginSave(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        TEST_TEXTAREA = self.getDriver().find_element_by_id(TEST_TEXTAREA_ID)
        TEST_TEXTAREA.send_keys(TEST_TEST_ADD)
        self.getDriver().find_element_by_id(BTN_SAVE_CONFIG).click()
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        result = self.driver.execute_script(TEST_SCRIPT_RETURN_VALUE)
        self.assertEqual(result, VALID_CONFIG_AFTER_SAVING)
        self.driver.execute_script(TEST_SCRIPT_CHANGE_VAL)
