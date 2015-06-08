from unittest import TestCase
from configparser import ConfigParser
from configparser import  SafeConfigParser
import os
import sys

sys.path.append('../')
import config_reader


HOST = 'localhost'
PORT = 27017
DBNAME = 'geomongo'
INSTANCEPREFIX = 'instance'


class TestConfingParser(TestCase):
    def testHost(self):
    	self.assertEqual(HOST, config_reader.getHost())
    def testPort(self):
    	self.assertEqual(PORT, config_reader.getPort())
    def testDbName(self):
    	self.assertEqual(DBNAME, config_reader.getDbName())
    def testInstancePrefix(self):
    	self.assertEqual(INSTANCEPREFIX, config_reader.getInstancePrefix())
