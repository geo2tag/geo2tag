from js_qunit_tests_wrapper import JsQUnitTestsWrapper


class TestInstaceTest(JsQUnitTestsWrapper):

    def testInstace(self):
        self.checkTestPage(self.getUrl('/instance/tests'))
