from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName

# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]

COLLECTION = 'services'

def addTag(tag):
    db[TAGS].insert(tag)

#    def getNearTags(self, latitude, longitude):
def  getServiceById(id):
    obj = db[COLLECTION].find_one({'_id' : id})
    if obj != None:
        return obj
    return getReturnObject()
