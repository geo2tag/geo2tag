import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from basic_selenium_test import BasicSeleniumTest
IMG_CLASS = ".google_authorized"


class TestLoginResource(BasicSeleniumTest):

    def testLoginResource(self):
        URL = self.getUrl('/instance/login')
        self.driver.get(URL)
        self.driver.implicitly_wait(30)
        obj = self.driver.find_element_by_css_selector(IMG_CLASS)
        self.assertNotEquals(obj, None)
