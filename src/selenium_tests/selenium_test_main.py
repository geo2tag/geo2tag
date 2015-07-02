import unittest
from basic_selenium_test import BasicSeleniumTest
import sys
from test_GT_1340_login_resurce import TestLoginResource
sys.path.append('../../')
def main(host):
    suite = unittest.TestSuite()
    suite.addTest(BasicSeleniumTest.parametrize(TestLoginResource, param=host))
    returnCode = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(returnCode)

if __name__ == '__main__':
    host = sys.argv[1]
    main(host)