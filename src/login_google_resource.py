from flask_restful import reqparse
from flask.ext.restful import Resource
from config_reader import getGoogleClientID, getGoogleClientSecret, getGoogleRedirectUrl 
from flask_oauth import OAuth
from flask import Blueprint
from url_utils import getPathWithPrefix
from urllib2 import Request, urlopen, URLError
from json import loads
from user_routines import addUser, logUserIn

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

AUTHORIZED_URL = '/login/google/authorized' 


def processGoogleData(data):
    EMAIL = 'email'
    _ID = 'id'
    FIRST_NAME = 'given_name'
    LAST_NAME  = 'family_name'
    userDict = loads (data)
    return addUser(userDict[_ID], userDict[FIRST_NAME], userDict[LAST_NAME], userDict[EMAIL])
    

@google_oauth.route(getPathWithPrefix(AUTHORIZED_URL))
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                None, headers)
    try:
        res = urlopen(req)
    except URLError, e:
        if e.code == 401:
        # Unauthorized - bad token
           return 'Error1'
        return res.read()
    _id = processGoogleData(res.read())
    logUserIn(_id) 

    return session['user_id']

