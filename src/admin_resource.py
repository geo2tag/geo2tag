from debug_info_resource import getDebugInfo
from flask_restful import Resource
from flask import render_template
from flask import make_response


class AdminResource(Resource):

    def get(self):
        return make_response(
            render_template(
                'admin.html',
                instance_prefix='instance',
                debug_info=getDebugInfo()
            )
        )
