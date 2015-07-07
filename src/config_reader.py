from configparser import ConfigParser
from configparser import  SafeConfigParser
import os
CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))+'/config.ini'
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
GOOGLE_CLIENT_ID_KEY = '599917606278-5drdaru9i21nk7q0s3h5k95dchausmne.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET_KEY = 'rzGBHKuBfXdCcmg4Vwn7mVCR'

def getConfigParser():
    config = SafeConfigParser({OPTION_HOST:HOST,OPTION_PORT:PORT,OPTION_DBNAME:DBNAME,OPTION_INSTANCEPREFIX:INSTANCEPREFIX,OPTION_DEBUG_USERS:DEBUG_USERS, GOOGLE_CLIENT_ID: GOOGLE_CLIENT_ID_KEY, GOOGLE_CLIENT_SECRET: GOOGLE_CLIENT_SECRET_KEY})
    config.read(CONFIG_PATH)
    return config
	
def getHost():
    return getConfigParser().get(SECTION,OPTION_HOST) 

def getPort():
    return int(getConfigParser().get(SECTION,OPTION_PORT))

def getDbName():
    return getConfigParser().get(SECTION,OPTION_DBNAME) 

def getInstancePrefix():
    return getConfigParser().get(SECTION,OPTION_INSTANCEPREFIX)
   	
def getDebugUsers():
    str = getConfigParser().get(SECTION,OPTION_DEBUG_USERS)
    list = str.split(',')
    return list

def getGoogleClientID():
    return getConfigParser().get(GOOGLE_SECTION,GOOGLE_CLIENT_ID) 

def getGoogleClientSecret():
    return str(getConfigParser().get(GOOGLE_SECTION,GOOGLE_CLIENT_SECRET))
