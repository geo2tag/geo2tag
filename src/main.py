from login_google_authorized_resource import LoginGoogleAuthorizedResource, AUTHORIZED_URL
from login_google_resource import LoginGoogleResource
from point_resource import PointResource
from flask import Flask, current_app
from flask.ext.restful import Resource, Api
from service_resource import ServiceResource
from service_list_resource import ServiceListResource
from status_resource import StatusResource
from log_resource import LogResource
from debug_info_resource import DebugInfoResource
from flask import make_response
from bson import json_util
from channels_list_resource import ChannelsListResource
from channel_resource import ChannelResource
from point_list_resource import PointListResource
from login_resource import LoginResource
from url_utils import getPathWithPrefix

def output_json(obj, code, headers=None):
    if isinstance(obj, str) == True:
        return make_response(obj, code)
    return make_response(json_util.dumps(obj), code)

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
app = Flask(__name__)
app.secret_key='11121212121'
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS


api.add_resource(ServiceResource, getPathWithPrefix('/service/<string:serviceName>'))
api.add_resource(StatusResource, getPathWithPrefix('/status'))
api.add_resource(ServiceListResource, getPathWithPrefix('/service'))
api.add_resource(DebugInfoResource, getPathWithPrefix('/debug_info'))
api.add_resource(LogResource, getPathWithPrefix('/service/<string:serviceName>/log'),
                              getPathWithPrefix('/log'))
api.add_resource(ChannelsListResource, getPathWithPrefix('/service/<string:serviceName>/channel'))
api.add_resource(ChannelResource, getPathWithPrefix('/service/<string:serviceName>/channel/<string:channelId>'))

api.add_resource(PointResource, getPathWithPrefix('/service/<string:serviceName>/point/<string:pointId>'))
api.add_resource(PointListResource, getPathWithPrefix('/service/<string:serviceName>/point'))
api.add_resource(LoginResource, getPathWithPrefix('/login'))
api.add_resource(LoginGoogleAuthorizedResource, getPathWithPrefix('/login/google/authorized'))
api.add_resource(LoginGoogleResource, getPathWithPrefix('/login/google'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
