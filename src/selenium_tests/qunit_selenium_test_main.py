import unittest
from js_qunit_tests_wrapper import JsQUnitTestsWrapper
import sys
from test_instance_internal_tests import TestInstaceInternalTest
from test_instance_tests import TestInstaceTest
sys.path.append('../../')


def main(host):
    suite = unittest.TestSuite()
    suite.addTest(JsQUnitTestsWrapper.parametrize(TestInstaceTest, param=host))
    suite.addTest(JsQUnitTestsWrapper.parametrize(TestInstaceInternalTest, param=host))
    returnCode = not unittest.TextTestRunner(
        verbosity=2).run(suite).wasSuccessful()
    sys.exit(returnCode)

if __name__ == '__main__':
    host = sys.argv[1]
    main(host)
