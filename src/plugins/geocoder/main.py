from job_resource import JobResource
from geocoding_job_list_resource import GeocodingJobListResource


def getPluginResources():
    return {'service/<string:serviceName>/job': GeocodingJobListResource,
            'service/<string:serviceName>/job/<string:jobId>': JobResource}


def getPluginInfo():
    return 'Plugin that imports data from Open Karelia'

