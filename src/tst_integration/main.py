import unittest
import sys
from basic_integration_test import BasicIntegrationTest 
from test_status_request import TestStatusRequest
from test_request_delete import TestStatusRequestDelete

def main(host):
    suite = unittest.TestSuite()
    suite.addTest(BasicIntegrationTest.parametrize(TestStatusRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestStatusRequestDelete, param=host))

    returnCode = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(returnCode)

if __name__ == '__main__':
    host = sys.argv[1]
    main(host)
