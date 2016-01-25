from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/admin/plugin'
TEST_CLASS_BTN_CONFIG = '.btn-config-plugin'
TEST_CLASS_NAME_SELECTOR = '.name-config-plugin'
TEST_CONFIG = '/config/'


class TestCheckConfigPluginBtn(BasicSeleniumTest):

    def testCheckConfigPluginBtn(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        BTN = self.getDriver().find_elements_by_css_selector(
            TEST_CLASS_BTN_CONFIG)[0]
        NAME = self.getDriver().find_elements_by_css_selector(
            TEST_CLASS_NAME_SELECTOR)[0].text
        BTN.click()
        self.assertEquals(
            self.getDriver().current_url,
            str(URL) + TEST_CONFIG + NAME)
