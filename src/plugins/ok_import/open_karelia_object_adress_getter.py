import sys
sys.path.append('../../open_data_import')
from open_data_object_address_getter import OpenDataObjectAddressGetter

class OpenKareliaObjectAddressGetter(OpenDataObjectAddressGetter):
	def getAdress(self, obj):
		return obj.site