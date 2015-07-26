from unittest import TestCase
from  service_not_found_exception import ServiceNotFoundException
from db_model import possibleException
import sys
sys.path.append('../')

TEST_VALID_EXCEPTION = ServiceNotFoundException
TEST_NOT_VALID_EXCEPTION = ArithmeticError
TEST_VALID_TUPLE = ('Service not found', 404)
TEST_NOT_VALID_EXCEPTION_STRING = 'This is not valid exception'

@possibleException
def funcForTesting(Exc):
    raise Exc(TEST_NOT_VALID_EXCEPTION_STRING)

class TestPossibleExceptionDecorator(TestCase):
    def testPossibleExceptionDecorator(self):
        self.assertEqual(funcForTesting(TEST_VALID_EXCEPTION), TEST_VALID_TUPLE)
        with self.assertRaises(TEST_NOT_VALID_EXCEPTION) as context:
        	funcForTesting(TEST_NOT_VALID_EXCEPTION)
        self.assertTrue(TEST_NOT_VALID_EXCEPTION_STRING in context.exception)        
