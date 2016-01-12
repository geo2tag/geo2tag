from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest

TEST_URL = 'instance/admin/service/test_id'


class TestAdminServiceResource(BasicSeleniumTest):

    def testcheckAdminResource(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        WebDriverWait(self.getDriver(), 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, "body"))
        )
        res = self.getDriver().find_element_by_tag_name("h2")
        self.assertNotEquals(res, None)
        res = self.getDriver().find_element_by_tag_name("body")
        self.assertNotEquals(res, None)
        res = self.getDriver().find_element_by_tag_name("head")
        self.assertNotEquals(res, None)
