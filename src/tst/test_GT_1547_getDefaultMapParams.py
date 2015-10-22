#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from map_resource import getDefaultMapParams

SERVICE_NAME = 'testservice'
TEST_ID = '556721a52a2e7febd2744200'
CHANNEL_IDS = 'channel_ids'


class TestgetDefaultMapParams(TestCase):

    def testgetDefaultMapParams(self):
        result = getDefaultMapParams(SERVICE_NAME)
        self.assertEqual(result[CHANNEL_IDS][0], TEST_ID)
