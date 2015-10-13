from possible_exception import possibleException
from flask.ext.restful import Resource
from job_manager import JobManager

class JobResource(Resource):

    @possibleException
    def get(self, serviceName, jobId):
        return JobManager.getJob(jobId)

    @possibleException
    def delete(self, serviceName, jobId):
        return JobManager.stopJob(jobId)