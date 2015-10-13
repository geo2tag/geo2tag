from possible_exception import possibleException
<<<<<<< HEAD
import flask_restful as restful
from flask_restful import Resource
sys.path.append('/var/www/geomongo/plugins/ok_import/')
=======
from flask.ext.restful import Resource
>>>>>>> origin/master
from job_manager import JobManager


class JobResource(Resource):

    @possibleException
    def get(self, serviceName, jobId):
        return JobManager.getJob(jobId)

    @possibleException
    def delete(self, serviceName, jobId):
        return JobManager.stopJob(jobId)
