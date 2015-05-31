#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

from  service_not_found_exception import ServiceNotFoundException

class test_ServiceNotFoundException(unittest.TestCase):
    def test_ServiceNotFoundException_func(self):
        mas = []
        try:
            mas[1] = 1
        except Exception, e:
            ServiceException = ServiceNotFoundException(e)
            self.assertTrue(('Service not found', 400) == ServiceException.getReturnObject())