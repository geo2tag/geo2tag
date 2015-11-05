from basic_selenium_test import BasicSeleniumTest


class TestAdminResource(BasicSeleniumTest):

    def testAdminResource(self):
        URL = self.getUrl('/instance/admin')
        BasicSeleniumTest.getDriver().get(URL)
        BasicSeleniumTest.getDriver().implicitly_wait(30)
        obj = BasicSeleniumTest.getDriver().find_element_by_css_selector(".admin-header")
        self.assertNotEquals(obj, None)
