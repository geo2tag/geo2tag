from flask_restful import reqparse
from flask.ext.restful import Resource
from config_reader import getGoogleClientID, getGoogleClientSecret, getGoogleRedirectUrl 
from flask_oauth import OAuth

oauth = OAuth()

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
