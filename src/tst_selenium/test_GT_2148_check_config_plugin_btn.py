from basic_selenium_test import BasicSeleniumTest

TEST_URL = 'instance/admin/plugin'
TEST_CLASS_BTN_CONFIG = '.btn-config-plugin'
TEST_CLASS_NAME_SELECTOR = '.name-config-plugin'
TEST_CONFIG = '/config/'


class TestCheckConfigPluginBtn(BasicSeleniumTest):

    def testCheckConfigPluginBtn(self):
        URL = self.getUrl(TEST_URL)
        driver = self.getDriver()
        driver.get(URL)
        driver.implicitly_wait(30)
        BTN = driver.find_elements_by_css_selector(
            TEST_CLASS_BTN_CONFIG)[0]
        NAME = driver.find_elements_by_css_selector(
            TEST_CLASS_NAME_SELECTOR)[0].text
        BTN.click()
        main_window = driver.current_window_handle
        driver.switch_to_window(driver.window_handles[1])
        self.assertEquals(
            driver.current_url,
            str(URL) + TEST_CONFIG + NAME)
        driver.switch_to_window(main_window)
