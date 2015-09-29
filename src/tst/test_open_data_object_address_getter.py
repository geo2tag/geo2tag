import unittest
from open_data_object_address_getter import OpenDataObjectAddressGetter

TEST_DATA = [1,2,3,4]


class ConcreteTestCalss(OpenDataObjectAddressGetter):

    def getAddress(self, obj):
        return obj


class TestOpenDataObjectAddressGetter(unittest.TestCase):

    def testOpenDataObjectAddressGetter(self):
        test = ConcreteTestCalss()
        self.assertEquals(test.getAddressList(TEST_DATA), TEST_DATA)
