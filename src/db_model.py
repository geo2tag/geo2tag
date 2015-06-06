from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
import pymongo
from datetime import datetime
from  service_not_found_exception import ServiceNotFoundException

# getLog constants
COLLECTION_LOG_NAME = "log"
FIND_AND_SORT_KEY = "date"

# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]
COLLECTION = 'services'
NAME = 'name'
CONFIG = 'config'
LOG_SIZE = 'log_size'
OWNERID = 'owner_id'
ID = '_id'
# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]
COLLECTION = 'services'

def addTag(tag):
    db[TAGS].insert(tag)

def addService(name, logSize, ownerld):
    obj = db[COLLECTION].find_one({NAME: name})
    if obj != None:
        return False
    obj_id = db[COLLECTION].save({NAME : name, CONFIG : {LOG_SIZE : logSize}, OWNERID : ownerld})
    if obj_id == None:
        return None
    else:
        return obj_id

def getServiceList(number, offset):
    return {}

#    def getNearTags(self, latitude, longitude):

def getLog(dbName, number, offset, dateFrom, dateTo) :
    collection = db[COLLECTION_LOG_NAME]
    #if collection.count() == 0
    #   collection.drop()
    #   return None
    number = 0 if (number == None or number < 0) else number
    offset = 0 if (offset == None or offset < 0) else offset
    if (dateFrom == None and dateTo == None) :
        return None
    elif dateFrom == None :
        return collection.find({FIND_AND_SORT_KEY : {"$lte" : dateTo}}, None, offset, number).sort(FIND_AND_SORT_KEY, pymongo.ASCENDING)    
    elif dateTo == None :
        return collection.find({FIND_AND_SORT_KEY : {"$gte" : dateFrom}}, None, offset, number).sort(FIND_AND_SORT_KEY, pymongo.ASCENDING)
    else :
        if dateFrom > dateTo :
            return None
        return collection.find({FIND_AND_SORT_KEY : {"$gte" : dateFrom , "$lte" : dateTo}}, None, offset, number).sort(FIND_AND_SORT_KEY, pymongo.ASCENDING)

def  getServiceIdByName(name):
    obj = db[COLLECTION].find_one({NAME : name})
    if obj != None:
        return obj
    raise ServiceNotFoundException()

def  getServiceById(id):
    obj = db[COLLECTION].find_one({ID : id})
    if obj != None:
        return obj
    raise ServiceNotFoundException()
