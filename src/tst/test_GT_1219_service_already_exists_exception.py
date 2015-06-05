#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('../')
from service_already_exists_exception import ServiceAlreadyExistsException

class TestServiceAlreadyExistsException(TestCase):
    def testServiceAlreadyExistsException(self):
        with self.assertRaises(ServiceAlreadyExistsException) as e:
        	raise ServiceAlreadyExistsException()      	
