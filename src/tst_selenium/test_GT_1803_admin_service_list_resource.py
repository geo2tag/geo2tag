from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest

TEST_URL = 'instance/admin/service'
H2 = "Services"


class TestAdminServiceListResource(BasicSeleniumTest):

    def testcheckAdminResource(self):
        URL = self.getUrl(TEST_URL)
        BasicSeleniumTest.getDriver().get(URL)
        WebDriverWait(BasicSeleniumTest.getDriver(), 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, "body"))
        )
        res = BasicSeleniumTest.getDriver().find_element_by_tag_name("h2")
        self.assertEqual(res.text, H2)
        res = BasicSeleniumTest.getDriver().find_element_by_tag_name("body")
        self.assertNotEquals(res, None)
        res = BasicSeleniumTest.getDriver().find_element_by_tag_name("head")
        self.assertNotEquals(res, None)
