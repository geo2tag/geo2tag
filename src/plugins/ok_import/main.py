import sys
from job_resource import JobResource
from job_resource_by_id import JobResourceById
def getPluginResources():
    return {'service/<string:serviceName>/job': JobResource, 'service/<string:serviceName>/job/<string:job_id>': JobResourceById}

def getPluginInfo():
    return 'Plugin that imports data from Open Karelia'
