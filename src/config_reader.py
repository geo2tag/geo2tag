from configparser import ConfigParser

CONFIG_PATH = '../config/config.ini'
SECTION = 'main'
OPTION_HOST = 'host'
OPTION_PORT = 'port'
OPTION_DBNAME = 'db_name'
OPTION_INSTANCEPREFIX = 'instanceprefix'

HOST = 'localhost'
PORT = 27017
DBNAME = 'geomongo'
INSTANCEPREFIX = 'instance'

def getConfigParser():
	config = ConfigParser()
	config.read(CONFIG_PATH)
	return config
	
def getHost():
	return getConfigParser().get(SECTION,OPTION_HOST) if getConfigParser().has_option(SECTION,OPTION_HOST) else HOST

def getPort():
    return getConfigParser().get(SECTION,OPTION_PORT) if getConfigParser().has_option(SECTION,OPTION_PORT) else PORT

def getDbName():
    return getConfigParser().get(SECTION,OPTION_DBNAME) if getConfigParser().has_option(SECTION,OPTION_DBNAME) else DBNAME

def getInstancePrefix():
	return getConfigParser().get(SECTION,OPTION_INSTANCEPREFIX) if getConfigParser().has_option(SECTION,OPTION_INSTANCEPREFIX) else INSTANCEPREFIX
   	
 
