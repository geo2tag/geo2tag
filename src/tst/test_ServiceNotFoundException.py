#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from service_not_exist_exception import ServiceNotExistException


class TestServiceNotExistException(unittest.TestCase):

    def testServiceNotExistException(self):
        with self.assertRaises(ServiceNotExistException):
            raise ServiceNotExistException()
