from flask_restful import reqparse
from flask.ext.restful import Resource
from config_reader import getGoogleClientID, getGoogleClientSecret, getGoogleRedirectUrl 
from flask_oauth import OAuth
from flask import Blueprint, session
from url_utils import getPathWithPrefix
from urllib2 import Request, urlopen, URLError
from json import loads
from user_routines import addUser, logUserIn
from possible_exception import possibleException
from authorization_error import AuthorizationError

AUTHORIZED_URL = '/login/google/authorized' 
oauth = OAuth()
google_oauth = Blueprint('google_oauth', __name__)
google = oauth.remote_app('google',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                          'response_type': 'code'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_key=getGoogleClientID(),
    consumer_secret=getGoogleClientSecret())

class LoginGoogleResource(Resource):
    def get(self):
        print "getGoogleRedirectUrl() {0}".format(getGoogleRedirectUrl())
        return google.authorize(callback=getGoogleRedirectUrl())


def processGoogleData(data):
    EMAIL = 'email'
    _ID = 'id'
    FIRST_NAME = 'given_name'
    LAST_NAME  = 'family_name'
    userDict = loads (data)
    return addUser(userDict[_ID], userDict[FIRST_NAME], userDict[LAST_NAME], userDict[EMAIL])
    

SUCCESS_MESSAGE = 'Success'

@google_oauth.route(getPathWithPrefix(AUTHORIZED_URL))
@google.authorized_handler
@possibleException
def authorized(resp):
    try:
        access_token = resp['access_token']
    except TypeError:
        raise AuthorizationError
    headers = {'Authorization': 'OAuth '+access_token}
    request = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                None, headers)
    res = urlopen(request)
    try:
        res = urlopen(request)
    except URLError, e:
        raise AuthorizationError
    _id = processGoogleData(res.read())
    logUserIn(_id) 

    return SUCCESS_MESSAGE

