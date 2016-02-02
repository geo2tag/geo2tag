# -*- coding: utf-8 -*-
from basic_selenium_test import BasicSeleniumTest
from time import sleep


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
        self.getDriver().implicitly_wait(30)
        serviceNameInput = self.getDriver().find_element_by_id(SERVICE_NAME)
        serviceNameInput.send_keys(NON_EXISTENT_SERVICE)
        sleep(2)
        serviceList = self.getDriver().find_element_by_id(SERVICE_LIST)
        self.assertEquals(serviceList.get_attribute('innerHTML'), '')
#
#    def testServiceDelete(self):
#        URL = self.getUrl('/instance/admin/service')
#        SERVICE_URL = 'service_url'
#        self.getDriver().get(URL)
#
        # HACK REPLACE ME WITH https://geo2tag.atlassian.net/browse/GT-2186
        # solution
#        self.getDriver().\
#            find_element_by_css_selector('.page-link.next')
#
#        serviceNames = self.getDriver().\
#            find_elements_by_class_name(SERVICE_URL)
#        self.assertNotEqual(len(serviceNames), 0)
#        firstService = serviceNames[0]
#
#        firstServiceName = unicode(firstService.get_attribute('innerHTML'))
#
#        deleteButton = self.getDriver().\
#            find_element_by_id('delete_' + firstServiceName)
#        deleteButton.click()
#        successAlert = self.getDriver().\
#            find_element_by_class_name('alert-success')
#        validText = u'<a href="#"' + \
#            u' class="close" data-dismiss="alert"' + \
#            u' aria-label="close">×</a><strong>' + \
#            firstServiceName + \
#            u' was deleted successfully</strong>'
#        alertText = successAlert.get_attribute('innerHTML')
#        self.assertEquals(alertText, validText)
