from basic_selenium_test import BasicSeleniumTest

ADMIN_URL = '/instance/admin'
RAW_HREFS = 'row admin-header'
GEOMONGO = 'Geomongo'


class TestGT1776AdminTemplate(BasicSeleniumTest):
    def testGT1776AdminTemplate(self):
        self.driver.implicitly_wait(5)
        self.driver.get(self.getUrl(ADMIN_URL))
        self.assertTrue(GEOMONGO in self.driver.title)
        self.driver.find_element_by_css_selector('.raw')

