# -*- coding: utf-8 -*-
from basic_selenium_test import BasicSeleniumTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import requests
import json

TEST_URL = 'instance/admin/plugin'
TEST_URL_LIST_PLUGIN = 'instance/plugin'
TEST_CLASS_NAME_SELECTOR = '.name-config-plugin'
TEST_URL_MANAGE = 'instance/manage_plugins?'
TEST_ENABLED = u'enabled'
ENABLED = 'Enabled'
DISABLED = 'Disabled'


class TestCheckUnablePluginBtn(BasicSeleniumTest):

    def getPluginStatus(self, pluginName):
        response = requests.get(self.getUrl(TEST_URL_LIST_PLUGIN))
        responseDict = json.loads(response._content)
        pluginEntry = responseDict[pluginName]
        pluginStatus = pluginEntry[TEST_ENABLED]
        return pluginStatus

    def testCheckUnablePluginBtn(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        NAME = self.getDriver().find_elements_by_css_selector(
            TEST_CLASS_NAME_SELECTOR)[0].text
        BUTTON_SELECTOR = '[plugin_name="' + NAME + '"]'
        pluginStatus = self.getPluginStatus(NAME)
        self.assertIs(type(pluginStatus), bool)
        VALID_RESULT = not pluginStatus

        if pluginStatus:
            VALID_STATUS_TEXT = ENABLED
        elif not pluginStatus:
            VALID_STATUS_TEXT = DISABLED

        BTN = self.getDriver().find_element_by_css_selector(
            BUTTON_SELECTOR)
        BTN.click()

        print "Plugin status = {}, VALID_STATUS_TEXT = {}". \
            format(pluginStatus, VALID_STATUS_TEXT)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.CSS_SELECTOR, BUTTON_SELECTOR), VALID_STATUS_TEXT)
        )

        pluginStatus = self.getPluginStatus(NAME)
        self.assertEqual(pluginStatus, VALID_RESULT)
