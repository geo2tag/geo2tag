import sys
sys.path.append('../../open_data_import')
from open_data_object_address_getter import OpenDataObjectAddressGetter

SITE = 'site'


class OpenKareliaObjectAddressGetter(OpenDataObjectAddressGetter):

    def getAddress(self, obj):
        return obj[SITE]
