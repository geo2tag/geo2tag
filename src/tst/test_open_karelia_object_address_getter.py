import sys
import unittest
sys.path.append('../plugins/ok_import')
from open_karelia_object_adress_getter import OpenKareliaObjectAddressGetter

TEST_DATA = [1,2,3,4]


class TestOpenKareliaObjectAddressGetter(unittest.TestCase):

    def testOpenKareliaObjectAddressGetter(self):
        test = OpenKareliaObjectAddressGetter()
        test.getAdress(10)