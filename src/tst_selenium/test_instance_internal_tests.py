import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from js_qunit_tests_wrapper import JsQUnitTestsWrapper


class TestInstaceInternalTest(JsQUnitTestsWrapper):

    def testInstaceInternal(self):
        self.checkTestPage(self.getUrl('/instance/internal_tests'))
