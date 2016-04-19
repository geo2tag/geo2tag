from unittest import TestCase
from icon_resource import getColorsFromChannelId

TEST_CHANNEL_ID = u'556721a52a2e7febd2744200'
TEST_VALID_RESULT = 'a45489'


class TestGenerateMarkerSvgCode(TestCase):

    def testGenerateMarkerSvgCode(self):
        res = getColorsFromChannelId(TEST_CHANNEL_ID)
        self.assertEqual(TEST_VALID_RESULT, res)
