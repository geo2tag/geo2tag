from unittest import TestCase
from base_geo2tag_exception import BaseGeo2TagException
from base_exception import BaseException
from possible_exception import possibleException

TEST_DATA = 'test data'

class testException(BaseGeo2TagException):
    def getReturnObject(self):
        return TEST_DATA



@possibleException
def testFunc():
    if (False is True):
        return None
    raise testException()

class TestPossibleExceptinoFix(TestCase):
    def testPossibleExceptinoFix(self):
        self.assertEqual(testFunc(), TEST_DATA)


