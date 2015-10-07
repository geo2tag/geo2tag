import sys
from geocoding_job_list_resource import GeocodingJobListResource
sys.path.append('/var/www/geomongo/open_data_import')


def getPluginResources():
    return {'service/<string:serviceName>/job': GeocodingJobListResource}


def getPluginInfo():
    return 'Plugin that imports data from Open Karelia'
