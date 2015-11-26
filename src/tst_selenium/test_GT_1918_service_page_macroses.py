from basic_selenium_test import BasicSeleniumTest

TEST_URL = 'instance/admin/service/test_id'
INTEGER_INPUT = 'integer_input_log_size'
AUTOCOMPLITE_INPUT = 'autocomplite_owner_id'


class TestAdminServiceMacroses(BasicSeleniumTest):

    def testAdminServiceMacroses(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        res = self.getDriver().find_element_by_id(INTEGER_INPUT)
        self.assertNotEquals(res, None)
        res = self.getDriver().find_element_by_id(AUTOCOMPLITE_INPUT)
        self.assertNotEquals(res, None)
