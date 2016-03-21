from point_list_resource import PointListResource
from jsonld_converter import convertPointsToJsonLD


class SmartM3Resource(PointListResource):

    def get(self, serviceName):
        filteredList = super(SmartM3Resource, self).get(serviceName)
        return convertPointsToJsonLD(filteredList)
