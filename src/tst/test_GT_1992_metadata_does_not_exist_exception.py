#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from metadata_does_not_exist_exception import MetadataDoesNotExistException


class TestMetadataDoesNotExistException(unittest.TestCase):

    def testMetadataDoesNotExistException(self):
        with self.assertRaises(MetadataDoesNotExistException):
            raise MetadataDoesNotExistException()
