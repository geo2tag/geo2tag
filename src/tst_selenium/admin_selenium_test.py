from basic_selenium_test import BasicSeleniumTest
from selenium.webdriver.common.keys import Keys


class AdminSeleniumTest(BasicSeleniumTest):

    def setUp(self):
        BasicSeleniumTest.setUp(self)
        driver = self.driver
        driver.get(self.getUrl('/'))

