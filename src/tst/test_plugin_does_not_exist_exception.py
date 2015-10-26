#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from plugin_does_not_exist_exception import PluginDoesNotExistException


class TestServiceNotExistException(unittest.TestCase):

    def testServiceNotExistException(self):
        with self.assertRaises(PluginDoesNotExistException):
            raise PluginDoesNotExistException('plugin')
