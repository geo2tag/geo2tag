from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/service/testservice/map?longitude=1' + \
    '&latitude=1&zoom=17'


class TestJSONLayer(BasicSeleniumTest):

    def testJSONLayer(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        result = self.getDriver().find_elements_by_css_selector(
            ".leaflet-marker-pane img")
        self.assertNotEqual(0, len(result))
