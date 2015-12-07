from basic_selenium_test import BasicSeleniumTest


class TestAdminResource(BasicSeleniumTest):

    def testAdminResource(self):
        URL = self.getUrl('/instance/admin1')
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        obj = self.getDriver().find_element_by_css_selector(".admin-header")
        self.assertNotEquals(obj, None)
