from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest

TEST_URL = 'instance/login'
RESULT_LENGTH = 48
BASE_URL = 'url'
SCRIPT = "return getStaticUrl('" + BASE_URL + "');"


class TestCacheInvalidator(BasicSeleniumTest):

    def testCacheInvalidator(self):
        self.getDriver().get(self.getUrl(TEST_URL))
        WebDriverWait(self.getDriver(), 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, "head"))
        )
        result = self.getDriver().execute_script(SCRIPT)

        self.assertEqual(len(result), RESULT_LENGTH)
        self.assertEqual(result[0:len(BASE_URL)], BASE_URL)
