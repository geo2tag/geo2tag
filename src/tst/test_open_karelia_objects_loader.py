#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from open_karelia_objects_loader import OpenKareliaObjectsLoader
from requests.exceptions import ConnectionError


class Test_GT_1509_open_karelia_objects_loader(TestCase):

    def test_GT_1509_open_karelia_objects_loader(self):
        obj = OpenKareliaObjectsLoader(
           'http://geomongo/instance/service?number=1&offset=0')
        try:
            data = obj.load()
            self.assertNotEquals(data, None)
            self.assertNotEquals(data, '')
        except ConnectionError:
            print "Problem during data loading"   
