import sys
from job_resource import JobResource
from job_resource_by_id import JobResourceById


def getPluginResources():
    return {'service/<string:serviceName>/job': JobResource,
            'service/<string:serviceName>/job/<string:jobId>': JobResourceById}


def getPluginInfo():
    return 'Plugin that imports data from Open Karelia'
