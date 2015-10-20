#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from point_does_not_exist import PointDoesNotExist


class TestPointDoesNotExistException(TestCase):

    def testPointDoesNotExistException(self):
        with self.assertRaises(PointDoesNotExist):
            raise PointDoesNotExist()
