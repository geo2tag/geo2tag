from unittest import TestCase
from authorization_error import AuthorizationError


class TestAuthorizationFail(TestCase):

    def testAuthorizationFail(self):
        with self.assertRaises(AuthorizationError):
            raise AuthorizationError
