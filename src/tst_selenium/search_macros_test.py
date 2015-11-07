from js_qunit_tests_wrapper import JsQUnitTestsWrapper
SEARCH_FILED = 'input[name="search-substring"]'
SEARCH_BUTTON = 'input[name="search-substring-submit"]'


class TestMacrosSearchTest(JsQUnitTestsWrapper):

    def testMacrosSearchTest(self):
        self.checkTestPage(self.getUrl('/instance/macros_tests'))
        obj = self.getDriver().find_element_by_css_selector(SEARCH_FILED)
        self.assertNotEquals(obj, None)
        obj = self.getDriver().find_element_by_css_selector(SEARCH_BUTTON)
        self.assertNotEquals(obj, None)
