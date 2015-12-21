from basic_selenium_test import BasicSeleniumTest


class TestServiceListResource(BasicSeleniumTest):

    def testServiceListResource(self):
        ELEMENT_IDS = ['create_new_service', 'service_name',
                       'service_list', 'autocomplite_owner_id']
        URL = self.getUrl('/instance/admin/service')
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        for elementId in ELEMENT_IDS:
            obj = self.getDriver().find_element_by_id(elementId)
            self.assertNotEquals(obj, None)

    def testFormImmidiateUpdate(self):
        URL = self.getUrl('/instance/admin/service')
        SERVICE_NAME = 'service_name'
        SERVICE_LIST = 'container_service_list'
        NON_EXISTENT_SERVICE = 'NON_EXISTENT_SERVICE'
        self.getDriver().get(URL)
        serviceNameInput = self.getDriver().find_element_by_id(SERVICE_NAME)
        serviceNameInput.send_keys(NON_EXISTENT_SERVICE)
        serviceList = self.getDriver().find_element_by_id(SERVICE_LIST)
        self.assertEquals(serviceList.get_attribute('innerHTML'), '')
