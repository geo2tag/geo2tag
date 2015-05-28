from flask import Flask, current_app
from flask.ext.restful import Resource, Api
from service_resource import ServiceResource
from status_resource import StatusResource
from config_reader import getInstancePrefix

app = Flask(__name__)
api = Api(app)

def getPathWithPrefix(str):
    path = '/'+getInstancePrefix()+str
    return path

api.add_resource(ServiceResource, getPathWithPrefix('/service/<string:serviceName>'))
api.add_resource(StatusResource, getPathWithPrefix('/status'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
