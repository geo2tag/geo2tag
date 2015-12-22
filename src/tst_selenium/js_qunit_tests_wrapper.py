from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest


class JsQUnitTestsWrapper(BasicSeleniumTest):

    def checkTestResult(self, testResult):
        self.assertNotEquals(testResult, None)

    def checkTestPage(self, pageRelativeUrl):
        driver = self.getDriver()
        self.getDriver().implicitly_wait(30)
        driver.get(pageRelativeUrl)
        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "qunit-testresult"), 'Tests completed in')
        )
        # Checking <span class="failed">0</span>
        res = driver.find_element_by_class_name("container")
        self.checkTestResult(res)
        failed_number_element = driver.find_element_by_class_name("failed")
        failed_number = failed_number_element.get_attribute("innerHTML")
        self.assertEquals(int(failed_number), 0)
