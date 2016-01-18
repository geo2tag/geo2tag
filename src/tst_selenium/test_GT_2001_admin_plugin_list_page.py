# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest

TEST_URL = 'instance/admin/plugin'
H2 = "Плагины"


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
        self.assertNotEquals(res, None)
        res = self.driver.find_element_by_tag_name("head")
        self.assertNotEquals(res, None)
