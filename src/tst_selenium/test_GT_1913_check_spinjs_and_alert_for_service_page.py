from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/admin/service/test_id'
TEST_BTN_SAVE_ID = 'save_service_btn'
TEST_LOG_SIZE_ID = 'integer_input_log_size'
TEST_DATA = 0
TEST_NOT_VALID_DATA = 'test_string'
TEST_ALERT_CLASS = 'alert-success'
TEST_MSG = u' Saving is finished successfully'
TEST_MSG_ERROR = u' Saving is finished unsuccessfully error: 400'
TEST_SCRIPT_SUCCESS = "return $('.alert-success').text()"
TEST_SCRIPT_ERROR = "return $('.alert-danger').text()"
TEST_SCRIPT_SPIN = "return $('.spinner').length"


class TestCheckSpinjsAndAlertForServicePage(BasicSeleniumTest):

    def testCheckSpinjsAndAlertForServicePage(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        result = self.driver.execute_script(TEST_SCRIPT_SPIN)
        self.assertEqual(result, 0)
        self.driver.find_element_by_id(TEST_LOG_SIZE_ID).send_keys(TEST_DATA)
        self.driver.find_element_by_id(TEST_BTN_SAVE_ID).click()
        alert = self.driver.switch_to_alert()
        alert.accept()
        result = self.driver.execute_script(TEST_SCRIPT_SUCCESS)
        self.assertEqual(result, TEST_MSG)

    def testBadScenarioForServicePage(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        logsize = self.driver.find_element_by_id(TEST_LOG_SIZE_ID)
        logsize.send_keys(TEST_NOT_VALID_DATA)
        self.driver.find_element_by_id(TEST_BTN_SAVE_ID).click()
        result = self.driver.execute_script(TEST_SCRIPT_ERROR)
        self.assertEqual(result, TEST_MSG_ERROR)
