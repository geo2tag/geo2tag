import sys
sys.path.append('../../open_data_import')
from open_data_object_adress_getter import OpenDataObjectAddressGetter

class OpenKareliaObjectAddressGetter(OpenDataObjectAddressGetter):
	def getAdress(obj):
		return obj.site