from unittest import TestCase
from test_performance import main

CREATE_JOB_LINK = 'http://not_valid_link'
JOB_DATA = \
    '{"channelName":"testchannel",' \
    '"openDataUrl":"http://mobile.openkarelia.org//get_nearest_objects?' \
    'latitude=61.787458487564&longitude=34.362810647964", ' \
    '"showObjectUrl":"", "showImageUrl":""} '
VIEW_JOB_LINK = \
    'http://geomongo/instance/plugin/ok_import/service/testservice/job'
JOB_COUNT = 1
TIMEOUT = 1
TEST_ANS = 1


class test_GT_1578testPerfomance(TestCase):

    def test_GT_1578testPerfomance(self):
        ans = main(
            CREATE_JOB_LINK,
            JOB_DATA,
            VIEW_JOB_LINK,
            JOB_COUNT,
            TIMEOUT)
        self.assertEquals(TEST_ANS, ans)
