from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/service/testservice/map?refresh=0'
TEST_CHECKBOX_SELECTOR = '.leaflet-control-layers-selector'
TYPE = 'type'
CHECKBOX = 'checkbox'
CHECKED = 'checked'


class TestCheckAllCheckboxesAreChecked(BasicSeleniumTest):

    def testCheckAllCheckboxesAreChecked(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        list_checkboxes = self.getDriver().find_elements_by_css_selector(
            TEST_CHECKBOX_SELECTOR)
        for ch in list_checkboxes:
            if ch.get_attribute(TYPE) == CHECKBOX:
                self.assertTrue(ch.get_attribute(CHECKED))
