#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
from bson.objectid import ObjectId
from db_model import getDbObject
sys.path.append('../plugins/ok_import/')
from open_karelia_data_to_points_loader import OpenKareliaDataToPointsLoader
POINTS = 'points'
ID = '_id'
TEST_SERVICE = 'testservice'
pointsList = [
    {
        "_id": ObjectId("552833515c0dd1178d37f7ee"), "location": {
            "type": "Point", "coordinates": [
                24, 4.4]}, "name": "point_GT_1509_1"}, {
                    "_id": ObjectId("552833515c0dd1178d37f7ff"), "location": {
                        "type": "Point", "coordinates": [
                            24, 4.4]}, "name": "point_GT_1509_2"}]


class Test_GT_1509_class_open_data_to_points_loader(TestCase):

    def test_GT_1509_class_open_data_to_points_loader(self):
        dataObj = OpenKareliaDataToPointsLoader(TEST_SERVICE, pointsList)
        dataObj.loadPoints()
        collection = getDbObject(TEST_SERVICE)[POINTS]
        self.assertNotEquals(None, collection.find_one(
            {ID: ObjectId("552833515c0dd1178d37f7ee")}))
        self.assertNotEquals(None, collection.find_one(
            {ID: ObjectId("552833515c0dd1178d37f7ff")}))
        collection.remove({ID: ObjectId("552833515c0dd1178d37f7ee")})
        collection.remove({ID: ObjectId("552833515c0dd1178d37f7ff")})
        self.assertEquals(None, collection.find_one(
            {ID: ObjectId("552833515c0dd1178d37f7ee")}))
        self.assertEquals(None, collection.find_one(
            {ID: ObjectId("552833515c0dd1178d37f7ff")}))
