from basic_selenium_test import BasicSeleniumTest


class TestAdminResource(BasicSeleniumTest):

    def testAdminResource(self):
        URL = self.getUrl('/instance/admin')
        self.driver.get(URL)
        self.driver.implicitly_wait(30)
        obj = self.driver.find_element_by_css_selector(".admin-header")
        self.assertNotEquals(obj, None)
