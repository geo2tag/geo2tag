from flask_restful import reqparse
from flask.ext.restful import Resource
from config_reader import getGoogleClientID, getGoogleClientSecret, getGoogleRedirectUrl 
from flask_oauth import OAuth
from flask import Blueprint

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

#class LoginGoogleAuthorizedResource(Resource):
#    @google.authorized_handler
#    def get(self):

@google_oauth.route(REDIRECT_URI)
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

    return res.read()

