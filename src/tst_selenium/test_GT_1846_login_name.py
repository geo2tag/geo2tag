from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from basic_selenium_test import BasicSeleniumTest
import requests

TEST_URL = '/instance/login'
URL_LOGIN = 'instance/login/debug?_id=debug_user1'
URL_LOGOUT = '/instance/logout'
TEXT_ANONYMUS = 'Geo2Tag\nHello, Anonym \
| Login\nLogin with\nPowered by Geo2tag - geo2tag.com'
TEXT_USER = 'Geo2Tag\nHello, debug_user1 \
| Logout\nLogin with\nPowered by Geo2tag - geo2tag.com'


class TestAutorizedUser(BasicSeleniumTest):

    def testNoAutorizedUser(self):
        self.driver.get(self.getUrl(URL_LOGOUT))
        self.driver.get(self.getUrl(TEST_URL))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, "body"))
        )
        res = self.driver.find_element_by_class_name("container")
        self.assertEqual(res.text, TEXT_ANONYMUS)

    def testAutorizedUser(self):

        self.driver.get(self.getUrl(URL_LOGIN))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, "head"))
        )

        self.driver.get(self.getUrl(TEST_URL))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.TAG_NAME, "body"))
        )
        res = self.driver.find_element_by_class_name("container")
        self.assertEqual(res.text, TEXT_USER)
