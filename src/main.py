from flask import Flask, current_app
from flask.ext.restful import Resource, Api
from service_resource import ServiceResource
from service_list_resource import ServiceListResource
from status_resource import StatusResource
from config_reader import getInstancePrefix
from log_resource import LogResource
from debug_info_resource import DebugInfoResource

app = Flask(__name__)
api = Api(app)

def getPathWithPrefix(str):
    path = '/'+getInstancePrefix()+str
    return path

api.add_resource(ServiceResource, getPathWithPrefix('/service/<string:serviceName>'))
api.add_resource(StatusResource, getPathWithPrefix('/status'))
api.add_resource(ServiceListResource, getPathWithPrefix('/service/'))
api.add_resource(DebugInfoResource, getPathWithPrefix('/debug_info/'))

api.add_resource(LogResource, '/'+getInstancePrefix()+'/service/<string:serviceName>/log',
	                          '/'+getInstancePrefix()+'/log')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)