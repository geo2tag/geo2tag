from ok_import_resource_parser import OKImportParser
from thread_job import ThreadJob
from open_karelia_import import openKareliaImport
import sys
sys.path.append('../')
sys.path.append('/var/www/geomongo/open_data_import')
from job_list_resource_factory import JobListResourceFactory

<<<<<<< HEAD
JobListResource = JobListResourceFactory(OKImportParser, ThreadJob, openKareliaImport)
=======

class JobListResource(Resource):

    @possibleException
    def get(self, serviceName):
        getServiceIdByName(serviceName)
        return JobManager.getJobs()

    @possibleException
    def post(self, serviceName):
        job = OKImportParser.parsePostParameters()
        print job.get('importDataDict')
        channelName = job.get('channelName')
        getServiceIdByName(serviceName)
        getChannelByName(serviceName, channelName)
        thread = ThreadJob(openKareliaImport, job.get('channelName'),
                           job.get('openDataUrl'),
                           job.get('importDataDict'),
                           serviceName)

        return JobManager.startJob(thread)
>>>>>>> origin/GT-1656
