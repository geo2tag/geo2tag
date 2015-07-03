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

def getConfigParser():
    config = SafeConfigParser({OPTION_HOST:HOST,OPTION_PORT:PORT,OPTION_DBNAME:DBNAME,OPTION_INSTANCEPREFIX:INSTANCEPREFIX,OPTION_DEBUG_USERS:DEBUG_USERS})
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
