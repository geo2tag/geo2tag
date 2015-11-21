import unittest
import os
from pdocker import parse_string_time_to_timestamp
from pdocker import manage_script
from pdocker import write_log
from pdocker import LOG_NAME


class TestPdockerFunc(unittest.TestCase):
    def testParseStringTimeToTimestamp(self):
        res = parse_string_time_to_timestamp("1w")
        # seconds in one week
        self.assertEqual(res, (168 * 60 * 60))

    def testWriteLog(self):
        name = 'test_script'
        test_string = 'test_data'
        write_log(name, test_string)
        file_name = "/tmp/" + name.replace('/', '_') + LOG_NAME
        with open(file_name, 'rb') as log_file:
            res = log_file.readline()
        self.assertEqual(res, test_string)

    def testManageScript(self):
        r = manage_script('test', ['ls'])
        self.assertEqual(r, 0)