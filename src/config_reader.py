#from configparser import ConfigParser

'''CONFIG_PATH = 'config.ini'
SECTION = 'main'

def getConfigParser():
    return ConfigParser().read(CONFIG_PATH)'''

def getHost():
    return 'localhost'
    #return getConfigParser().get

def getPort():
    return 27017

def getDbName():
    return 'geomongo'

def getInstancePrefix():
    return 'instance'