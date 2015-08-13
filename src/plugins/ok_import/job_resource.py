from possible_exception import possibleException
from flask_restful import reqparse
from flask.ext.restful import Resource
from job_manager import JobManager
from ok_import_resource_parser import OKImportParser
from thread_job import ThreadJob

class JobResource(Resource):

    @possibleException
    def get(self, serviceName):
        return JobManager.getJobs()

    @possibleException
    def post(self, serviceName):
        job = OKImportParser.parsePostParameters()
        def stubFunction (channelName, openDataUrl, \
                          showObjectUrl, showImageUrl, \
                          serviceName):
            pass

        thread = ThreadJob(stubFunction, job.get('channelName'), \
                           job.get('openDataUrl'), \
                           job.get('showObjectUrl'), \
                           job.get('showImageUrl'), \
                           serviceName)

        return JobManager.startJob(thread)
