# -*- coding: utf-8 -*-
from manage_plugins_resource import ManagePluginsResource
from tests_resource import TestsResource
from point_resource import PointResource
from channels_list_resource import ChannelsListResource
from channel_resource import ChannelResource
from point_list_resource import PointListResource
from logout_resource import LogoutResource
from login_resource import LoginResource
from url_utils import getPathWithPrefix
from debug_login_resource import DebugLoginResource
from login_google_resource import LoginGoogleResource
from login_facebook_resource import LoginFacebookResource
from db_model import closeConnection
import atexit
from map_resource import MapResource
from plugin_list_resource import GetAllPluginsWithStatusResource
from internal_tests_resource import InternalTestsResource
from admin_log_resource import AdminLogResource
from admin_service_list_resource import AdminServiceListResource
from rest_api_routines import getApi, getApp, initApp, DEFAULT_REPRESENTATIONS
from log_resource import LogResource
from service_resource import ServiceResource
from service_list_resource import ServiceListResource
from status_resource import StatusResource
from debug_info_resource import DebugInfoResource
from admin_service_resource import AdminServiceResource
from user_find_resource import UserFindResource
from user_list_resource import UserListResource
from admin_resource import AdminResource
from plugin_config_resource import PluginConfigResource
from macros_test_resource import MacrosTestsResource

API = None


def addResources():
    getApi().representations = DEFAULT_REPRESENTATIONS
    getApi().add_resource(ChannelsListResource, getPathWithPrefix(
        '/service/<string:serviceName>/channel'))
    getApi().add_resource(ChannelResource, getPathWithPrefix(
        '/service/<string:serviceName>/channel/<string:channelId>'))
    getApi().add_resource(PointResource, getPathWithPrefix(
        '/service/<string:serviceName>/point/<string:pointId>'))
    getApi().add_resource(PointListResource, getPathWithPrefix(
        '/service/<string:serviceName>/point'))
    getApi().add_resource(LogoutResource, getPathWithPrefix('/logout'))
    getApi().add_resource(LoginResource, getPathWithPrefix('/login'))
    getApi().add_resource(LoginGoogleResource, getPathWithPrefix(
        '/login/google'))
    getApi().add_resource(LoginFacebookResource,
                          getPathWithPrefix('/login/facebook'))
    getApi().add_resource(DebugLoginResource, getPathWithPrefix(
        '/login/debug'))
    getApi().add_resource(TestsResource, getPathWithPrefix('/tests'))
    getApi().add_resource(AdminServiceListResource, getPathWithPrefix(
        '/admin/service'))
    getApi().add_resource(AdminServiceResource, getPathWithPrefix(
        '/admin/service/<service_id>'))
    getApi().add_resource(
        MapResource,
        getPathWithPrefix('/service/<string:serviceName>/map'))
    getApi().add_resource(
        GetAllPluginsWithStatusResource,
        getPathWithPrefix('/plugin'))
    getApi().add_resource(
        ManagePluginsResource,
        getPathWithPrefix('/manage_plugins'))
    getApi().add_resource(
        InternalTestsResource,
        getPathWithPrefix('/internal_tests'))
    getApi().add_resource(
        AdminResource,
        getPathWithPrefix('/admin'))
    getApi().add_resource(
        AdminLogResource,
        getPathWithPrefix('/admin/log'))
    getApi().add_resource(
        ServiceResource,
        getPathWithPrefix('/service/<string:serviceName>'))
    getApi().add_resource(
        StatusResource,
        getPathWithPrefix('/status'))
    getApi().add_resource(
        ServiceListResource,
        getPathWithPrefix('/service'))
    getApi().add_resource(
        DebugInfoResource,
        getPathWithPrefix('/debug_info'))
    getApi().add_resource(
        LogResource,
        getPathWithPrefix('/service/<string:serviceName>/log'),
        getPathWithPrefix('/log'))
    getApi().add_resource(
        UserFindResource,
        getPathWithPrefix('/user/<string:user_id>'))
    getApi().add_resource(
        PluginConfigResource,
        getPathWithPrefix('/plugin_config/<string:pluginName>'))
    getApi().add_resource(
        UserListResource,
        getPathWithPrefix('/user'))
    getApi().add_resource(
        MacrosTestsResource,
        getPathWithPrefix('/macros_tests'))

    # end of the list of imported resources

    atexit.register(closeConnection)

    initApp(getApi())

if __name__ == '__main__':
    addResources()
    getApp().run(host="0.0.0.0", port=5001, debug=True)
