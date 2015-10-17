import unittest
from open_karelia_object_address_getter import \
    OpenKareliaObjectAddressGetter, SITE

TEST_SITE = 'SITE'
TEST_OBJ = {SITE: TEST_SITE}


class TestOpenKareliaObjectAddressGetter(unittest.TestCase):

    def testOpenKareliaObjectAddressGetter(self):
        test = OpenKareliaObjectAddressGetter()
        self.assertEquals(test.getAddress(TEST_OBJ), TEST_SITE)
