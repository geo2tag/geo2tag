from basic_selenium_test import BasicSeleniumTest
import requests
import json

TEST_URL = 'instance/admin/plugin'
TEST_URL_LIST_PLUGIN = 'instance/plugin'
TEST_CLASS_NAME_SELECTOR = '.name-config-plugin'
TEST_URL_MANAGE = 'instance/manage_plugins?'
TEST_CLASS_DELETE_BTN = '.btn-delete-plugin'
TEST_ENABLED = u'enabled'


class TestCheckUnablePluginBtn(BasicSeleniumTest):

    def testCheckUnablePluginBtn(self):
        TEST_FLAG = False
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        NAME = self.getDriver().find_elements_by_css_selector(
            TEST_CLASS_NAME_SELECTOR)[0].text
        response = requests.get(self.getUrl(TEST_URL_LIST_PLUGIN))
        response = json.loads(response._content)
        for i in response:
            if i == NAME:
                if response[i][TEST_ENABLED] == False:
                    requests.get(self.getUrl(TEST_URL_MANAGE + NAME + '=True'))
                    TEST_FLAG = True
        BTN = self.getDriver().find_elements_by_css_selector(
            TEST_CLASS_DELETE_BTN)[0]
        BTN.click()
        response = requests.get(self.getUrl(TEST_URL_LIST_PLUGIN))
        response = json.loads(response._content)
        for i in response:
            if i == NAME:
                self.assertEqual(response[i][TEST_ENABLED], False)
        if not TEST_FLAG:
            requests.get(self.getUrl(TEST_URL_MANAGE + NAME + '=True'))
