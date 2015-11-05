from basic_selenium_test import BasicSeleniumTest
IMG_CLASS = ".google_authorized"


class TestLoginResource(BasicSeleniumTest):

    def testLoginResource(self):
        URL = self.getUrl('/instance/login')
        BasicSeleniumTest.getDriver().get(URL)
        BasicSeleniumTest.getDriver().implicitly_wait(30)
        obj = BasicSeleniumTest.getDriver().find_element_by_css_selector(IMG_CLASS)
        self.assertNotEquals(obj, None)
