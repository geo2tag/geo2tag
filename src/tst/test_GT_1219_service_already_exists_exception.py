#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('../')
from service_already_exists_exception import ServiceAlreadyExistsException

class TestServiceAlreadyExistsException(TestCase):
    def testServiceAlreadyExistsException(self):
        try:
            a = 1 / 0
        except Exception, e:
        	serviceException = ServiceAlreadyExistsException(e)
        	self.assertEqual(('Service already exists', 400), serviceException.getReturnObject())
        	
