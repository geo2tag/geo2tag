from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest

TEST_URL = 'instance/login'
RES = '?cache_inx'


class TestCacheInvalidator(BasicSeleniumTest):

    def testCacheInvalidator(self):
        self.getDriver().get(self.getUrl(TEST_URL))
        WebDriverWait(self.getDriver(), 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, "head"))
        )
        res = self.getDriver().execute_script("return getStaticUrl();")
        self.assertEqual(res, RES)
