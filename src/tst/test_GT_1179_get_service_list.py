from unittest import TestCase
import sys
sys.path.append('../')
from db_model import getServiceList
from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName


class GetServiceListTest(TestCase):
    def testGetServiceListTest(self):
        db = MongoClient(getHost(), getPort())[getDbName()]
        FIRST_OBJ = list(db['services'].find().sort('name', 1).skip(0).limit(1))[0]
        COUNT = db['services'].find().count()
        if COUNT > 1:
            LAST_OBJ = list(db['services'].find().sort('name', -1).skip(0).limit(1))[0]
            OBJECTS = list(db['services'].find())
            RESULT = getServiceList(0, COUNT)
            self.assertEqual(RESULT[0], FIRST_OBJ)
            self.assertEqual(RESULT[COUNT-1], LAST_OBJ)
            RESULT = getServiceList(None, None)
            self.assertEqual(RESULT[0], FIRST_OBJ)
            self.assertEqual(RESULT[COUNT-1], LAST_OBJ)

