#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from service_already_exists_exception import ServiceAlreadyExistsException


class TestServiceAlreadyExistsException(TestCase):

    def testServiceAlreadyExistsException(self):
        with self.assertRaises(ServiceAlreadyExistsException):
            raise ServiceAlreadyExistsException()
