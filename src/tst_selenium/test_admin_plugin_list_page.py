# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/admin/plugin'
H2 = u'Плагины'
LINE_XPATH = ".//*[@id='container_plugin_list']/hr"


class TestAdminPluginListPage(BasicSeleniumTest):

    def testCheckAdminPluginPage(self):
        URL = self.getUrl(TEST_URL)
        self.driver.get(URL)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, "body"))
        )
        res = self.driver.find_element_by_tag_name("h2")
        self.assertEqual(res.text, H2)
        res = self.driver.find_element_by_tag_name("body")
        self.assertNotNone(res)
        res = self.driver.find_element_by_tag_name("head")
        self.assertNotNone(res)

    def testCheckEnableButton(self):
        DISABLE = 'Disable'
        ENABLE = 'Enable'
        BUTTON_SELECTOR = '[plugin_name="ok_import"]'
        URL = self.getUrl(TEST_URL)
        self.driver.get(URL)

        button = self.driver.find_element_by_css_selector(
            BUTTON_SELECTOR)
        self.assertEquals(button.get_attribute('innerHTML'), DISABLE)

        button.click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.CSS_SELECTOR, BUTTON_SELECTOR), ENABLE)
        )

        button1 = self.driver.find_element_by_css_selector(
            BUTTON_SELECTOR)
        self.assertEquals(button1.get_attribute('innerHTML'), ENABLE)

    def testCheckLine(self):
        URL = self.getUrl(TEST_URL)
        self.driver.get(URL)
        result = self.driver.find_element_by_xpath(LINE_XPATH)
        self.assertNotNone(result)
