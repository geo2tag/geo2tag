from unittest import TestCase
import sys
sys.path.append('../')
from authorization_error import AuthorizationError

class TestAuthorizationFail(TestCase):
    def testAuthorizationFail(self):
        with self.assertRaises(AuthorizationError):
            raise AuthorizationError
