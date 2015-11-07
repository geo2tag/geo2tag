from basic_selenium_test import BasicSeleniumTest
IMG_CLASS = ".google_authorized"


class TestLoginResource(BasicSeleniumTest):

    def testLoginResource(self):
        URL = self.getUrl('/instance/login')
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        obj = self.getDriver().find_element_by_css_selector(IMG_CLASS)
        self.assertNotEquals(obj, None)
