#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from auto_build_image import compDate
from datetime import datetime

date1 = '2016-03-09 00:38:53'
date2 = '2016-03-04 00:38:53'


class TestAutoBuild(unittest.TestCase):

    def testCompDate(self):
        date_1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date_2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
        res = compDate(date_1, date_2)
        assertTrue(res)
