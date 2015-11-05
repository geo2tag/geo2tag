from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest


class JsQUnitTestsWrapper(BasicSeleniumTest):

    def checkTestResult(self, testResult):
        self.assertNotEquals(testResult, None)

    def checkTestPage(self, pageRelativeUrl):
        BasicSeleniumTest.getDriver().get(pageRelativeUrl)
        WebDriverWait(BasicSeleniumTest.getDriver(), 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "qunit-testresult"), 'Tests completed in')
        )
        res = BasicSeleniumTest.getDriver().find_element_by_class_name("container")
        self.checkTestResult(res)
