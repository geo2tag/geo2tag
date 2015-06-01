from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
from  service_not_found_exception import ServiceNotFoundException

# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]
COLLECTION = 'services'

def addTag(tag):
    db[TAGS].insert(tag)

#    def getNearTags(self, latitude, longitude):

def  getServiceIdByName(name):
    obj = db[COLLECTION].find_one({'name' : name})
    if obj != None:
        return obj
    raise ServiceNotFoundException()