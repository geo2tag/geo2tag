from basic_selenium_test import BasicSeleniumTest


class TestServiceListResource(BasicSeleniumTest):

    def testServiceListResource(self):
        ELEMENT_IDS = ['create_new_service', 'autocomplite_owner_id', 'service_name', 'service_list']
        URL = self.getUrl('/instance/service')
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        for elementId in ELEMENT_IDS:
            obj = self.getDriver().find_element_by_id(elementId)
            self.assertNotEquals(obj, None)
