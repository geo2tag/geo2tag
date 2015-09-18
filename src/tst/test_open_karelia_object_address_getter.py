import sys
import unittest
sys.path.append('../plugins/ok_import')
sys.path.append('../open_data_import')
from open_karelia_object_address_getter import OpenKareliaObjectAddressGetter

TEST_SITE = 'SITE'

class SiteClass:
    site = 'SITE'

class TestOpenKareliaObjectAddressGetter(unittest.TestCase):

    def testOpenKareliaObjectAddressGetter(self):
        test = OpenKareliaObjectAddressGetter()
        self.assertEquals(test.getAddress(SiteClass()), TEST_SITE)
