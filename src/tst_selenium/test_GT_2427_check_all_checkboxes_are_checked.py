from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/service/testservice/map'
TEST_SELECTOR = 'leaflet-control-layers-toggle'
TEST_CHECKBOX_SELECTOR = 'input.leaflet-control-layers-selector'



class TestCheckAllCheckboxesAreChecked(BasicSeleniumTest):

    def testCheckAllCheckboxesAreChecked(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        obj = self.getDriver().find_element_by_css_selector(TEST_SELECTOR)
        obj.click()
        list_checkboxes = self.getDriver().find_elements_by_css_selector(
            TEST_CHECKBOX_SELECTOR)
        
        
