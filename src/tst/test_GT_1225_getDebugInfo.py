from unittest import TestCase
import os
from debug_info_resource import getDebugInfo


RIGHT_FILE_NAME = os.path.dirname(os.path.realpath(__file__)) + "/../DEBUG"
TEST_FILE_DATA = ('''{
	'commit': COMMIT,
	'date' : DATE,
	'branch': BRANCH,
	'version': VERSION
}''')


def prepareDebugFile():
    file = open(RIGHT_FILE_NAME, "w+")
    file.write(TEST_FILE_DATA)


class TestGetDebugInfo(TestCase):

    def testGetDebugInfo(self):
        # checking if data from file is correct
        prepareDebugFile()
        self.assertEqual(getDebugInfo(), TEST_FILE_DATA)
        os.remove(RIGHT_FILE_NAME)
