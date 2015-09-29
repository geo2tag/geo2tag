from possible_exception import possibleException
from flask_restful import reqparse
from flask.ext.restful import Resource
from job_manager import JobManager
from ok_import_resource_parser import OKImportParser
from thread_job import ThreadJob
from open_karelia_import import openKareliaImport
import sys
sys.path.append('../')
from db_model import getChannelByName, getServiceIdByName


class JobListResource(Resource):

    @possibleException
    def get(self, serviceName):
        getServiceIdByName(serviceName)
        return JobManager.getJobs()

    @possibleException
    def post(self, serviceName):
        args = OKImportParser.parsePostParameters()
        channelName = args.get('channelName')
        getServiceIdByName(serviceName)
        getChannelByName(serviceName, channelName)
        thread = ThreadJob(openKareliaImport, args.get('channelName'),
                           args.get('openDataUrl'),
                           args,
                           serviceName)

        return JobManager.startJob(thread)
