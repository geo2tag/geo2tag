from possible_exception import possibleException
from flask_restful import Resource
from job_manager import JobManager
from db_model import getServiceIdByName


class JobResource(Resource):

    @possibleException
    def get(self, serviceName, jobId):
        getServiceIdByName(serviceName)
        return JobManager.getJob(jobId)

    @possibleException
    def delete(self, serviceName, jobId):
        getServiceIdByName(serviceName)
        return JobManager.stopJob(jobId)
