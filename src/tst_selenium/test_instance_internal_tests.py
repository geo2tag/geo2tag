from js_qunit_tests_wrapper import JsQUnitTestsWrapper

class TestInstaceInternalTest(JsQUnitTestsWrapper):
    def testInstaceInternal(self):
        self.checkTestPage(self.getUrl('/instance/internal_tests'))
