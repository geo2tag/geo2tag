import unittest
import sys
from basic_integration_test import BasicIntegrationTest 
from test_status_request import TestStatusRequest
from test_get_service_name import TestServiceGetRequest
from test_get_request import TestServiceListGetRequest
from test_put_service_name import TestServicePutRequest
from test_post_request import TestServiceListPostRequest

def main(host):
    suite = unittest.TestSuite()
    suite.addTest(BasicIntegrationTest.parametrize(TestStatusRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServicePutRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServiceListGetRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServiceListPostRequest, param=host))
    suite.addTest(BasicIntegrationTest.parametrize(TestServiceGetRequest, param=host))
    returnCode = not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(returnCode)

if __name__ == '__main__':
    host = sys.argv[1]
    main(host)
