import sys
from job_list_resource import JobListResource
sys.path.append('/var/www/geomongo/open_data_import')
from job_resource import JobResource


def getPluginResources():
    return {'service/<string:serviceName>/job': JobListResource,
            'service/<string:serviceName>/job/<string:jobId>': JobResource}


def getPluginInfo():
    return 'Plugin that imports data from Open Karelia'
