import unittest
from jobs_parser import areAllJobsDone, createJobStatistic, \
    getImportJobsText, parseJobs

URL = 'http://httpbin.org/status/200'
JSON_TEST = '{"_id": {"$oid": "55671ae113293c504d515a33"}, ' \
            '"config": {"log_size": 1048576, "logSize": 10},' \
            ' "name": "testservice", "owner_id": ""}'
JSON_RESULT = {
    u'_id': {
        u'$oid': u'55671ae113293c504d515a33'},
    u'config': {
        u'log_size': 1048576,
        u'logSize': 10},
    u'name': u'testservice',
             u'owner_id': u''}
JOBS_LIST1 = [
    {'openDataUrl': 'openDataUrl',
     'showObjectUrl': 'showObjectUrl',
     'channelName': 'channelName',
     'done': True,
     'time': '0:00:00.000913',
     'showImageUrl': 'showImageUrl',
     '_id': '66bMGe85Owtg',
     'serviceName': 'serviceName'},
    {'openDataUrl': 'openDataUrl',
     'showObjectUrl': 'showObjectUrl',
     'channelName': 'channelName',
     'done': False,
     'time': '0:00:00.000913',
     'showImageUrl': 'showImageUrl',
     '_id': '66bMGe85Owtg',
     'serviceName': 'serviceName'},
    {'openDataUrl': 'openDataUrl',
     'showObjectUrl': 'showObjectUrl',
     'channelName': 'channelName',
     'done': True,
     'time': '0:00:00.000913',
     'showImageUrl': 'showImageUrl',
     '_id': '66bMGe85Owtg',
     'serviceName': 'serviceName'}
]
JOBS_LIST2 = [
    {'openDataUrl': 'openDataUrl',
     'showObjectUrl': 'showObjectUrl',
     'channelName': 'channelName',
     'done': True,
     'time': '0:00:00.000913',
     'showImageUrl': 'showImageUrl',
     '_id': '66bMGe85Owtg',
     'serviceName': 'serviceName'},
    {'openDataUrl': 'openDataUrl',
     'showObjectUrl': 'showObjectUrl',
     'channelName': 'channelName',
     'done': True,
     'time': '0:00:00.000913',
     'showImageUrl': 'showImageUrl',
     '_id': '66bMGe85Owtg',
     'serviceName': 'serviceName'},
    {'openDataUrl': 'openDataUrl',
     'showObjectUrl': 'showObjectUrl',
     'channelName': 'channelName',
     'done': True,
     'time': '0:00:00.000913',
     'showImageUrl': 'showImageUrl',
     '_id': '66bMGe85Owtg',
     'serviceName': 'serviceName'}
]

JOB_STATISTIC_TEST = \
    [{"openDataUrl": "http://mobile.openkarelia.org//get_nearest_objects?"
        "latitude=61.787458487564&longitude=34.362810647964",
        "showObjectUrl": "",
        "channelName": "test_GT_1286",
        "done": True,
        "time": "0:00:03.846279",
        "showImageUrl": "",
        "_id": "FaBKKA05Xvoc",
        "serviceName": "testservice"},
        {"openDataUrl": "http://mobile.openkarelia.org//get_nearest_objects?"
            "latitude=61.787458487564&longitude=34.362810647964",
            "showObjectUrl": "",
            "channelName": "test_GT_1286",
            "done": True,
            "time": "0:00:04.895279",
            "showImageUrl": "",
            "_id": "FaBKKA05Xvoc",
            "serviceName": "testservice"},
        {"openDataUrl":
            "http://mobile.openkarelia.org//get_nearest_objects?"
            "latitude=61.787458487564&longitude=34.362810647964",
            "showObjectUrl": "",
            "channelName": "test_GT_1286",
            "done": True,
            "time": "0:00:03.84523",
            "showImageUrl": "",
            "_id": "FaBKKA05Xvoc",
            "serviceName": "testservice"}]
STATISTIC_RESULT = {
    'average': {
        'value': '0:00:04.419559'}, 'min': {
            'value': '00:00:03.845230', 'job': JOB_STATISTIC_TEST}, 'max': {
                'value': '00:00:04.895279', 'job': JOB_STATISTIC_TEST}}


class TestJobsParser(unittest.TestCase):

    def testGetImportJobsText(self):
        self.assertEquals(getImportJobsText(URL), '')

    def testParseJobs(self):
        self.assertEquals(parseJobs(JSON_TEST), JSON_RESULT)

    def testAreAllJobsDone(self):
        self.assertEquals(areAllJobsDone(JOBS_LIST1), False)
        self.assertEquals(areAllJobsDone(JOBS_LIST2), True)

    def testCreateJobStatistic(self):
        self.assertEquals(
            createJobStatistic(JOB_STATISTIC_TEST),
            STATISTIC_RESULT)
