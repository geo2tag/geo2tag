from geocoding_job_list_resource import GeocodingJobListResource


def getPluginResources():
    return {'service/<string:serviceName>/job': GeocodingJobListResource}


def getPluginInfo():
    return 'Plugin that imports data from Open Karelia'

