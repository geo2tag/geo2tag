from db_model import addPoints



DB = "testservice"
COLLECTION = "points"
ID = "_id"
NAME = 'name'
TEST_POINT1 = {'lat':1.1, 'lon':10, 'alt':1.1, 'json':'d', 'channel_id':'3'}
TEST_POINT2 = {'lat':1.2, 'lon':20, 'alt':1.1, 'json':'a', 'channel_id':'5'}

res = addPoints(DB, [TEST_POINT1, TEST_POINT2])
print res