from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/admin/service/testservice'
TEST_SCRIPT_RETURN_H2_VALUE = 'return $("#service_h2_id").text()'
TEST_SCRIPT_RETURN_LOG_SIZE_VALUE = 'return $("#integer_input_log_size").text()'
TEST_LOG_SIZE_VALUE = 10
TEST_H2 = 'Service testservice'
TEST_LOG_SIZE_VALUE_NEW = ''
TEST_H2_NEW = 'New service testservice'

class TestCheckDisplayDataServicePage(BasicSeleniumTest):

    def testCheckDisplayDataServicePage(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
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
