from flask import Flask, current_app
from flask.ext.restful import Resource, Api
from service_resource import ServiceResource
from config_reader import getInstancePrefix

app = Flask(__name__)
api = Api(app)

api.add_resource(ServiceResource, '/'+getInstancePrefix()+'/service/<string:serviceName>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
