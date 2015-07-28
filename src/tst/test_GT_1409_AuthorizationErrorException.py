from unittest import TestCase
import sys
sys.path.append('../')
from authorization_error import AuthorizationError

class TestAuthorizationError(TestCase):
    def testAuthorizationError(self):
        with self.assertRaises(AuthorizationError):
            raise AuthorizationError
