from flask_restful import Resource
from flask_oauth import OAuth
from flask import Blueprint, session, request
from config_reader import getFacebookClientID,\
    getFacebookClientSecret, getFacebookRedirectUrl
from url_utils import getPathWithPrefix
from possible_exception import possibleException


AUTHORIZED_URL = '/login/facebook/authorized'
oauth = OAuth()
facebook_oauth = Blueprint('facebook_oauth', __name__)
facebook = oauth.remote_app(
    'facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://facebook.com/dialog/oauth',
    consumer_key=getFacebookClientID(),
    consumer_secret=getFacebookClientSecret(),
    request_token_params={'scope': 'email'}
)


class LoginFacebookResource(Resource):

    def get(self):
        print "getFacebookRedirectUrl() {0}".format(getFacebookRedirectUrl())
        return facebook.authorize(callback=getFacebookRedirectUrl())


SUCCESS_MESSAGE = 'Success'


@facebook_oauth.route(getPathWithPrefix(AUTHORIZED_URL))
@facebook.authorized_handler
@possibleException
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    # userID = facebook.get('/me')
    return SUCCESS_MESSAGE


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')
