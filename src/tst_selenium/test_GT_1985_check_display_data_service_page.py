from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/admin/service/testservice'
TEST_URL_NEW = '/instance/admin/service/notvalidservicename'
TEST_SCRIPT_RETURN_H2_VALUE = 'return $("#service_h2_id").text()'
TEST_SCRIPT_RETURN_LOG_SIZE_VALUE = 'return $("#integer_input_log_size").val()'
TEST_LOG_SIZE_VALUE = u'10'
TEST_H2 = u'Service testservice'
TEST_LOG_SIZE_VALUE_NEW = u''
TEST_H2_NEW = u'New service notvalidservicename'


class TestCheckDisplayDataServicePage(BasicSeleniumTest):

    def testCheckDisplayDataServicePage(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        self.driver.implicitly_wait(30)
        result = self.driver.execute_script(TEST_SCRIPT_RETURN_LOG_SIZE_VALUE)
        self.assertEqual(result, TEST_LOG_SIZE_VALUE)
        result = self.driver.execute_script(TEST_SCRIPT_RETURN_H2_VALUE)
        self.assertEqual(result, TEST_H2)
        URL = self.getUrl(TEST_URL_NEW)
        self.getDriver().get(URL)
        result = self.driver.execute_script(TEST_SCRIPT_RETURN_LOG_SIZE_VALUE)
        self.assertEqual(result, TEST_LOG_SIZE_VALUE_NEW)
        result = self.driver.execute_script(TEST_SCRIPT_RETURN_H2_VALUE)
        self.assertEqual(result, TEST_H2_NEW)
