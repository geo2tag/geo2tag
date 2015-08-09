import sys
from job_resource import JobResource

def getPluginResources():
    return {'service/<serviceName>/job': JobResource}

def getPluginInfo():
    return 'Plugin that imports data from Open Karelia'