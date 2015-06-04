#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

from  service_not_found_exception import ServiceNotFoundException

class TestServiceNotFoundException(unittest.TestCase):
    def testServiceNotFoundException(self):
        with self.assertRaises(ServiceNotFoundException) as e:
            raise ServiceNotFoundException()