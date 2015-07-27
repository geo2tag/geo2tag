#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

from  service_not_exist_exception import ServiceNotExistException

class TestServiceNotExistException(unittest.TestCase):
    def testServiceNotExistException(self):
        with self.assertRaises(ServiceNotExistException) as e:
            raise ServiceNotExistException()