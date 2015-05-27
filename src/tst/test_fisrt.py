#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from not_existing_module import not_existing_class
class TestFirst(TestCase):
    def testFirst(self):
        print 'First test'
        self.assertTrue(True)
