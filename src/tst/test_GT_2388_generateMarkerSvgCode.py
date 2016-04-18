from unittest import TestCase
from map_resource import generateMarkerSvgCode

TEST_CHANNEL_ID = u'556721a52a2e7febd2744200'
TEST_RADIUS = '13'
TEST_MARKER = {'x': '1', 'y': '1'}
TEST_VALID_RESULT = '<svg><circle cx="1" cy="1" r="13" ' + \
    'transform="matrix(1 0 0 1 0 0)" style="fill: rgb("a4", "54", "89"); ' + \
    'cursor: move;"></circle></svg>'


class TestGenerateMarkerSvgCode(TestCase):

    def testGenerateMarkerSvgCode(self):
        res = generateMarkerSvgCode(TEST_MARKER, TEST_RADIUS, TEST_CHANNEL_ID)
        print res
