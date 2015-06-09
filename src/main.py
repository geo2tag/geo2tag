from flask import Flask, current_app
from flask.ext.restful import Resource, Api
from service_resource import ServiceResource
from service_list_resource import ServiceListResource
from status_resource import StatusResource
from config_reader import getInstancePrefix
from debug_info_resource import DebugInfoResource
from flask import make_response
from bson import json_util
import json

def output_json(obj, code, headers=None):
    if isinstance(obj, str) == True:
        resp = make_response(dumps(obj), code)
        resp.headers.extend(headers or {}) 
    elif isinstance(obj, dict):
        return json.loads(json_util.dumps(obj))

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
app = Flask(__name__)
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS

api.add_resource(ServiceResource, '/'+getInstancePrefix()+'/service/<string:serviceName>')
api.add_resource(StatusResource, '/'+getInstancePrefix()+'/status')
api.add_resource(ServiceListResource, '/'+getInstancePrefix()+'/service/')
api.add_resource(DebugInfoResource, '/'+getInstancePrefix()+'/debug_info/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)