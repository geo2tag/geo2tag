import unittest
import sys
from basic_selenium_test import BasicSeleniumTest
from test_GT_1635_status_OK import TestStatusOK

def main(host):
    suite = unittest.TestSuite()
    suite.addTest(BasicSeleniumTest.parametrize(TestStatusOK, param=host))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    host = sys.argv[1]
    main(host)
