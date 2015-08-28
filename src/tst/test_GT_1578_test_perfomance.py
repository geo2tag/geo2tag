from unittest import TestCase
import sys
sys.path.append('../../scripts/perfomance/od_perfomance')
from test_perfomance import main

class test_GT_1578testPerfomance(TestCase):

    def test_GT_1578testPerfomance(self):
        ans = main('http://geomongo/instance/plugin/ok_import/service/testservice/job',
                   '{"channelName":"testchannel","openDataUrl":"http://mobile.openkarelia.org//get_nearest_objects?latitude=61.787458487564&longitude=34.362810647964", "showObjectUrl":"", "showImageUrl":""} ',
                   'http://geomongo/instance/plugin/ok_import/service/testservice/job',
                    2,
                    2)
        self.assertEquals(0, ans)

