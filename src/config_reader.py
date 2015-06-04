from configparser import ConfigParser
from configparser import  SafeConfigParser
import os
CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))+'/config.ini'
SECTION = 'main'
OPTION_HOST = 'host'
OPTION_PORT = 'port'
OPTION_DBNAME = 'db_name'
OPTION_INSTANCEPREFIX = 'instance_prefix'

HOST = 'localhost'
PORT = 27017
DBNAME = 'geomongo'
INSTANCEPREFIX = 'instance'

def getConfigParser():
	config = SafeConfigParser({OPTION_HOST:HOST,OPTION_PORT:str(PORT),OPTION_DBNAME:DBNAME,OPTION_INSTANCEPREFIX:INSTANCEPREFIX})
	config.read(CONFIG_PATH)
	return config
	
def getHost():
	return getConfigParser().get(SECTION,OPTION_HOST) 

def getPort():
    return getConfigParser().get(SECTION,OPTION_PORT)

def getDbName():
    return getConfigParser().get(SECTION,OPTION_DBNAME) 

def getInstancePrefix():
	return getConfigParser().get(SECTION,OPTION_INSTANCEPREFIX)
   	
 
