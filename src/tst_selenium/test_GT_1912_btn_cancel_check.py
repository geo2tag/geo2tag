from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/admin/service'
TEST_CLASS_NAME = '.container'
TEST_BTN_CLASS_NAME = '.btn-danger'


class TestBtnCancelCheck(BasicSeleniumTest):

    def testBtnCancelCheck(self):
        URL = self.getUrl(TEST_URL)
        driver = self.getDriver()
        driver.get(URL)
        services = driver.find_elements_by_tag_name('h3')
        services[len(services)-1].click()
        btn = driver.find_element_by_css_selector(TEST_BTN_CLASS_NAME)
        btn.click()
        url = driver.current_url
        index = url.rfind('//')
        self.assertEqual(url[index+1:], TEST_URL)
