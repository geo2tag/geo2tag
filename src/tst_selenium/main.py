import unittest
import sys
from basic_selenium_test import BasicSeleniumTest
from test_GT_1635_status_OK import TestStatusOK
from test_GT_1340_login_resurce import TestLoginResource
from test_instance_tests import TestInstaceTest
from test_instance_internal_tests import TestInstaceInternalTest

def main(host):
    suite = unittest.TestSuite()
    suite.addTest(BasicSeleniumTest.parametrize(TestStatusOK, param=host))
    suite.addTest(BasicSeleniumTest.parametrize(TestLoginResource, param=host))
    suite.addTest(BasicSeleniumTest.parametrize(TestInstaceTest, param=host))
    suite.addTest(BasicSeleniumTest.parametrize(TestInstaceInternalTest, param=host))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    host = sys.argv[1]
    main(host)
