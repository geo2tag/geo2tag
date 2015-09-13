#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')
from point_list_resource_parser import parseBcParametr

INARGS = [{'lat': 1.1, 'lon': 1.1, 'alt': 5, 'json': {}, 'channel_id': ''}]
OUTARGS = [{'lat': 1.1, 'lon': 1.1, 'alt': 5,
            'json': {}, 'channel_id': '', 'bc': False}]

INARGS1 = [{'lat': 1, 'bc': True}]
OUTARGS1 = [{'lat': 1, 'bc': True}]


class TestValidatePointsList(unittest.TestCase):

    def testValidatePointsList(self):
        args = parseBcParametr(INARGS)
        self.assertEqual(args, OUTARGS)
        args = parseBcParametr(INARGS1)
        self.assertEqual(args, OUTARGS1)
