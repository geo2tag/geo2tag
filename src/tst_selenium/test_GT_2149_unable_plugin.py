from basic_selenium_test import BasicSeleniumTest
import requests
import json

TEST_URL = 'instance/admin/plugin'
TEST_URL_LIST_PLUGIN = 'instance/plugin'
TEST_CLASS_NAME_SELECTOR = '.name-config-plugin'


class TestCheckUnablePluginBtn(BasicSeleniumTest):
    
    def testCheckUnablePluginBtn(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        NAME = self.getDriver().find_elements_by_css_selector(
           TEST_CLASS_NAME_SELECTOR)[0].text
        response = requests.get(self.getUrl(TEST_URL_LIST_PLUGIN))
        response = json.loads(response)
        print response
