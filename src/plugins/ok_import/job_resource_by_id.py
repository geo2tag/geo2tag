from possible_exception import possibleException
from flask_restful import reqparse
from flask.ext.restful import Resource
from job_manager import JobManager
from ok_import_resource_parser import OKImportParser
from thread_job import ThreadJob

class JobResourceById(Resource):

    @possibleException
    def get(self, serviceName, jobId):
        return JobManager.getJob(job_id)

    @possibleException
    def delete(self, serviceName, jobId):
        return JobManager.stopJob(job_id)