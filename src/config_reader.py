from configparser import SafeConfigParser

import os
CONFIG_PATH = os.path.dirname(os.path.realpath(__file__)) + '/config.ini'

SECTION = 'main'
OPTION_HOST = 'host'
OPTION_PORT = 'port'
OPTION_DBNAME = 'db_name'
OPTION_INSTANCEPREFIX = 'instance_prefix'
OPTION_DEBUG_USERS = 'debug_users'

HOST = 'localhost'
PORT = 27017
DBNAME = 'geomongo'
INSTANCEPREFIX = 'instance'
DEBUG_USERS = ''

GOOGLE_SECTION = 'Google_OAuth'
GOOGLE_CLIENT_ID = 'GOOGLE_CLIENT_ID'
GOOGLE_CLIENT_SECRET = 'GOOGLE_CLIENT_SECRET'
GOOGLE_CLIENT_ID_KEY = '599917606278-5drdaru9i21nk7q0s3h5k95dchausmne.' + \
                       'apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET_KEY = 'rzGBHKuBfXdCcmg4Vwn7mVCR'
GOOGLE_REDIRECT_URL = 'GOOGLE_REDIRECT_URL'
GOOGLE_REDIRECT_URL_KEY = 'http://geomongo/instance/login/google/authorized'

GEONAMES_SECTION = 'geocoding'
GEONAMES_CLIENT_LOGIN = 'geonames_login'
GEONAMES_LOGIN = 'test'


def getConfigParser():
    config = SafeConfigParser({OPTION_HOST: HOST,
                               OPTION_PORT: PORT,
                               OPTION_DBNAME: DBNAME,
                               OPTION_INSTANCEPREFIX: INSTANCEPREFIX,
                               OPTION_DEBUG_USERS: DEBUG_USERS,
                               GOOGLE_CLIENT_ID: GOOGLE_CLIENT_ID_KEY,
                               GOOGLE_CLIENT_SECRET: GOOGLE_CLIENT_SECRET_KEY,
                               GOOGLE_REDIRECT_URL: GOOGLE_REDIRECT_URL_KEY,
                               GEONAMES_CLIENT_LOGIN: GEONAMES_LOGIN})
    config.read(CONFIG_PATH)
    return config


def getHost():
    return getConfigParser().get(SECTION, OPTION_HOST)


def getPort():
    return int(getConfigParser().get(SECTION, OPTION_PORT))


def getDbName():
    return getConfigParser().get(SECTION, OPTION_DBNAME)


def getInstancePrefix():
    return getConfigParser().get(SECTION, OPTION_INSTANCEPREFIX)


def getDebugUsers():
    str_users = getConfigParser().get(SECTION, OPTION_DEBUG_USERS)
    list_users = str_users.split(',')
    return list_users


def getGoogleClientID():
    return getConfigParser().get(GOOGLE_SECTION, GOOGLE_CLIENT_ID)


def getGoogleClientSecret():
    return str(getConfigParser().get(GOOGLE_SECTION, GOOGLE_CLIENT_SECRET))


def getGoogleRedirectUrl():
    return getConfigParser().get(GOOGLE_SECTION, GOOGLE_REDIRECT_URL)


def getGeonamesLogin():
    return getConfigParser().get(GEONAMES_SECTION, GEONAMES_CLIENT_LOGIN)
