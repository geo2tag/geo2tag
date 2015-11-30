from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/status'
TEST_XPATH = 'xhtml:html/xhtml:body/xhtml:pre'
VALID_STATUS = 'OK111'


class TestStatusOK(BasicSeleniumTest):

    def testStatusOK(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        STATUS = self.getDriver().find_element_by_xpath(TEST_XPATH)
        self.assertEquals(STATUS.text, VALID_STATUS)
