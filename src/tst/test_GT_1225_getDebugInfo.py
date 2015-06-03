from unittest import TestCase
import sys
import os
sys.path.append("../")
from debug_info_resource import getDebugInfo


RIGHT_FILE_NAME = os.path.dirname(os.path.realpath(__file__)) + "/DEBUG"
print RIGHT_FILE_NAME
TEST_FILE_DATA = ('''{
	'commit': COMMIT,
	'date' : DATE,
	'branch': BRANCH,
	'version': VERSIO
}''')

def prepareDebugFile() :
	file = open(RIGHT_FILE_NAME, "w")
	file.write(TEST_FILE_DATA)	

class TestGetDebugInfo(TestCase) :
	def testGetDebugInfo(self) :
		#checking if data from file is correct
		print "test for gebug info"
		prepareDebugFile()
		self.assertEqual(getDebugInfo(), TEST_FILE_DATA)
		os.remove(RIGHT_FILE_NAME)