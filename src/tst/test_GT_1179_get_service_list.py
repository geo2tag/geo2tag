from unittest import TestCase
from db_model import getServiceList, getDbObject
SERVICES = 'services'
NAME = 'name'
VALID_LENGTH = 1
TEST_OWNER_ID = 'new_test_ownerId'
TEST_SUBSTRING = 'test_service_name_1'


class GetServiceListTest(TestCase):

    def testGetServiceListTest(self):
        db = getDbObject()
        FIRST_OBJ = list(db[SERVICES].find().sort(NAME, 1).skip(0).limit(1))[0]
        COUNT = db[SERVICES].find().count()
        self.assertNotEqual(COUNT, 0)

        LAST_OBJ = list(
            db[SERVICES].find().sort(
                NAME, -1).skip(0).limit(1))[0]
        list(db[SERVICES].find())
        RESULT = getServiceList(COUNT, 0, None, None)
        self.assertEqual(RESULT[0], FIRST_OBJ)
        self.assertEqual(RESULT[COUNT - 1], LAST_OBJ)
        RESULT = getServiceList(None, 0, None, None)
        self.assertEqual(RESULT[0], FIRST_OBJ)
        self.assertEqual(RESULT[COUNT - 1], LAST_OBJ)
        RESULT = getServiceList(COUNT, 0, TEST_SUBSTRING, TEST_OWNER_ID)
        self.assertEqual(RESULT[0]['name'], TEST_SUBSTRING)
