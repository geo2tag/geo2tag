from flask import Flask, current_app
from flask.ext.restful import Resource, Api
from service_resource import ServiceResource
from status_resource import StatusResource
from config_reader import getInstancePrefix
from log_resource import LogResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ServiceResource, '/'+getInstancePrefix()+'/service/<string:serviceName>')
api.add_resource(StatusResource, '/'+getInstancePrefix()+'/status')

api.add_resource(LogResource, '/'+getInstancePrefix()+'/service/<string:serviceName>/log')
api.add_resource(LogResource, '/'+getInstancePrefix()+'/service/log')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
