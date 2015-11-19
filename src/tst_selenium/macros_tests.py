from js_qunit_tests_wrapper import JsQUnitTestsWrapper
SEARCH_FILED = 'input[name="search-substring"]'
SEARCH_BUTTON = 'input[name="search-substring-submit"]'


class TestMacroses(JsQUnitTestsWrapper):

    def testMacroses(self):
        self.checkTestPage(self.getUrl('/instance/macros_tests'))
