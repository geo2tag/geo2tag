from basic_selenium_test import BasicSeleniumTest
from selenium import webdriver
import requests

ADMIN_URL = 'instance/admin'
DEBUG_INFO_URL = 'instance/debug_info'
ADMIN_HEADER = '.admin-header *'
DEBUG_INFO = '.debuginfo'
INNER_HTML = 'innerHTML'
HREF = 'href'
GEOMONGO = 'Geomongo'
ADMIN_HEADER_ENTRIES = [
    ['/service', u'Service managment'],
    ['/user', u'User managment'],
    ['/plugin', u'Plugin managment'],
    ['/log', u'Instance logs']
]


class TestGT1776AdminTemplate(BasicSeleniumTest):

    def setUp(self):
        self.driver = webdriver.Firefox()
        for i in ADMIN_HEADER_ENTRIES:
            i[0] = unicode(self.getUrl(ADMIN_URL) + i[0])

    def tearDown(self):
        self.driver.close()

    def testGT1776AdminTemplateAdminHeaders(self):
        self.driver.implicitly_wait(5)
        self.driver.get(self.getUrl(ADMIN_URL))
        self.assertTrue(GEOMONGO in self.driver.title)
        for i in self.driver.find_elements_by_css_selector(ADMIN_HEADER):
            self.assertIn(
                [i.get_attribute(HREF), i.get_attribute(INNER_HTML)],
                ADMIN_HEADER_ENTRIES
            )

    def testGT1776AdminTemplateDebuginfo(self):
        self.driver.implicitly_wait(5)
        self.driver.get(self.getUrl(ADMIN_URL))
        self.assertTrue(GEOMONGO in self.driver.title)
        debug_info = self.driver.\
            find_element_by_css_selector(DEBUG_INFO).\
            get_attribute(INNER_HTML)
        r = requests.get(self.getUrl(DEBUG_INFO_URL))
        debug_info = debug_info.replace('\t', '')
        debug_info = debug_info.replace('\n', '')
        req_text = r.text.replace('\t', '')
        req_text = req_text.replace('\n', '')
        self.assertEqual(debug_info, req_text)
