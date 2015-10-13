from possible_exception import possibleException
from flask.ext.restful import Resource
from db_model import getChannelByName, getServiceIdByName
from job_manager import JobManager

def JobListResourceFactory(parserClass, jobClass, importFunction):
    class JobListResource(Resource):
 
        @possibleException
        def get(self, serviceName):
            getServiceIdByName(serviceName)
            return JobManager.getJobs()
 
        @possibleException
        def post(self, serviceName):
            importDataDict = parserClass.parsePostParameters()
            channelName = importDataDict.get('channelName')
            getServiceIdByName(serviceName)
            getChannelByName(serviceName, channelName)
            job = jobClass(importFunction, importDataDict.get('channelName'),
                           importDataDict.get('openDataUrl'), importDataDict,
                           serviceName)
 
            return JobManager.startJob(job)
 
    return JobListResource
