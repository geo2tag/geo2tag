from flask.ext.restful import Resource
from flask_oauth import OAuth
from flask import Blueprint
from config_reader import getFacebookClientID,\
    getFacebookClientSecret, getFacebookRedirectUrl
from url_utils import getPathWithPrefix
from urllib2 import Request, urlopen, URLError
from json import loads
from user_routines import addUser, logUserIn
from possible_exception import possibleException
from authorization_error import AuthorizationError


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


def processFacebookData(data):
    EMAIL = 'email'
    _ID = 'id'
    FIRST_NAME = 'given_name'
    LAST_NAME = 'family_name'
    userDict = loads(data)
    return addUser(
        userDict[_ID],
        userDict[FIRST_NAME],
        userDict[LAST_NAME],
        userDict[EMAIL])


SUCCESS_MESSAGE = 'Success'


@facebook_oauth.route(getPathWithPrefix(AUTHORIZED_URL))
@facebook.authorized_handler
@possibleException
def authorized(resp):
    try:
        access_token = resp['access_token']
    except TypeError:
        raise AuthorizationError
    headers = {'Authorization': 'OAuth ' + access_token}
    request = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                      None, headers)
    res = urlopen(request)
    try:
        res = urlopen(request)
    except URLError as e:
        raise AuthorizationError
    _id = processFacebookData(res.read())
    logUserIn(_id)

    return SUCCESS_MESSAGE
