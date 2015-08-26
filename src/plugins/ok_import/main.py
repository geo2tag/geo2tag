import sys
from job_list_resource import JobListResource
from job_resource import JobResource


def getPluginResources():
    return {'service/<string:serviceName>/job': JobListResource, 'service/<string:serviceName>/job/<string:jobId>': JobResource}


def getPluginInfo():
    return 'Plugin that imports data from Open Karelia'
