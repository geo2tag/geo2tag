from unittest import TestCase
from configparser import ConfigParser
from configparser import  SafeConfigParser
import os
import sys

sys.path.append('../')
CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))+'/DEBUG'
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

HOST = 'localhost'
PORT = 27017
DBNAME = 'geomongo'
INSTANCEPREFIX = 'instance'


class TestConfingParser(TestCase):
    def testHost(self):
    	self.assertEqual(HOST, getHost())
    def testPort(self):
    	self.assertEqual(str(PORT), getPort())
    def testDbName(self):
    	self.assertEqual(DBNAME, getDbName())
    def testInstancePrefix(self):
    	self.assertEqual(INSTANCEPREFIX, getInstancePrefix())
