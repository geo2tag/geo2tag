import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from basic_selenium_test import BasicSeleniumTest
import requests

class JsQUnitTestsWrapper(BasicSeleniumTest):
    def checkTestResult(self, testResult):
        self.assertNotEquals(testResult, None)

    def checkTestPage(self, pageRelativeUrl):
        self.checkTestResult(requests.get(pageRelativeUrl))