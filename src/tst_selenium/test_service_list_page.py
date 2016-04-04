# -*- coding: utf-8 -*-
from basic_selenium_test import BasicSeleniumTest
from time import sleep

LINE_XPATH = ".//*[@id='container_service_list']/hr"
INSTANCE_ADMIN = '/instance/admin/service'


class TestServiceListResource(BasicSeleniumTest):

    def testServiceListResource(self):
        ELEMENT_IDS = ['create_new_service', 'service_name',
                       'service_list', 'autocomplite_owner_id']
        URL = self.getUrl(INSTANCE_ADMIN)
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        for elementId in ELEMENT_IDS:
            obj = self.getDriver().find_element_by_id(elementId)
            self.assertNotEquals(obj, None)

    def testFormImmidiateUpdate(self):
        URL = self.getUrl(INSTANCE_ADMIN)
        SERVICE_NAME = 'service_name'
        SERVICE_LIST = 'container_service_list'
        NON_EXISTENT_SERVICE = 'NON_EXISTENT_SERVICE'
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        serviceNameInput = self.getDriver().find_element_by_id(SERVICE_NAME)
        serviceNameInput.send_keys(NON_EXISTENT_SERVICE)
        sleep(2)
        serviceList = self.getDriver().find_element_by_id(SERVICE_LIST)
        self.assertEquals(serviceList.get_attribute('innerHTML'), '')

    def testCheckLine(self):
        URL = self.getUrl(INSTANCE_ADMIN)
        self.getDriver().get(URL)
        result = self.getDriver().find_element_by_xpath(LINE_XPATH)
        self.assertIsNotNone(result, None)
#
#    def testServiceDelete(self):
#        URL = self.getUrl('/instance/admin/service')
#        SERVICE_URL = 'service_url'
#        self.getDriver().get(URL)
#        serviceNames = self.getDriver().\
#            find_elements_by_class_name(SERVICE_URL)
#        self.assertNotEqual(len(serviceNames), 0)
#        firstService = serviceNames[0]
#        firstServiceName = firstService.get_attribute('innerHTML')
#        deleteButton = self.getDriver().\
#            find_element_by_id('delete_' + firstServiceName)
#        deleteButton.click()
#        successAlert = self.getDriver().\
#            find_element_by_class_name('alert-success')
#        validText = '<strong> ' + \
#                    firstServiceName + \
#                    ' was deleted successfully</strong>'
#        alertText = successAlert.get_attribute('innerHTML')
#        self.assertEquals(alertText, validText)
