#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from auto_build_image import compDate
from datetime import datetime

date1 = '2016-03-09 00:38:53'
date2 = '2016-03-04 00:38:53'
date3 = '2016-03-19 00:35:54'


class TestAutoBuild(unittest.TestCase):

    def testCompDateTrue(self):
        date_1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date_2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
        res = compDate(date_1, date_2)
        self.assertTrue(res)

    def testCompDateFalse(self):
        date_1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date_3 = datetime.strptime(date3, "%Y-%m-%d %H:%M:%S")
        res = compDate(date_1, date_3)
        self.assertFalse(res)
