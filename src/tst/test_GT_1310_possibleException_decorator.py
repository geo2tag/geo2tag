from unittest import TestCase
from  service_not_found_exception import ServiceNotFoundException
from db_model import possibleException
import sys
sys.path.append('../')

TEST_VALID_EXCEPTION = ServiceNotFoundException
TEST_NOT_VALID_EXCEPTION = ArithmeticError
TEST_NOT_VALID_EXCEPTION_STRING = 'This is not valid exception'

@possibleException
def funcForTesting(Exc):
    raise Exc(TEST_NOT_VALID_EXCEPTION_STRING)

class TestPossibleExceptionDecorator(TestCase):
    def testPossibleExceptionDecorator(self):
        funcForTesting(TEST_VALID_EXCEPTION)
        with self.assertRaises(TEST_NOT_VALID_EXCEPTION) as context:
            funcForTesting(TEST_NOT_VALID_EXCEPTION)
        self.assertRaises(TEST_NOT_VALID_EXCEPTION_STRING in context.exception)
        
