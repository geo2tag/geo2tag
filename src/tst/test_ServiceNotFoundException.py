#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

from  service_not_found_exception import ServiceNotFoundException

class test_ServiceNotFoundException(unittest.TestCase):
    def test_ServiceNotFoundException_func(self):
        try:
            raise ServiceNotFoundException()
        except ServiceNotFoundException as e:
            self.assertEquals(('Service not found', 400), e.getReturnObject())