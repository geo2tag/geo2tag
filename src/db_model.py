from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
<<<<<<< HEAD
from  service_not_found_exception import ServiceNotFoundException
=======
import pymongo
from datetime import datetime

# getLog constants
COLLECTION_LOG_NAME = "log"
FIND_AND_SORT_KEY = "date"
>>>>>>> master

# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]
COLLECTION = 'services'
NAME = 'name'
CONFIG = 'config'
LOG_SIZE = 'log_size'
OWNERID = 'owner_id'

def addTag(tag):
    db[TAGS].insert(tag)

def addService(name, logSize, ownerld):
    obj = db[COLLECTION].find_one({'name' : name})
    if obj != None:
        return False
<<<<<<< HEAD
    db[COLLECTION].save({'name' : name, 'config' : {'log_size' : logSize}, 'owner_id' : ownerld})
    obj = db[COLLECTION].find_one({'name' : name})
    if obj == None:
        return None
    else:
        return obj['_id']
=======
    obj_id = db[COLLECTION].save({NAME : name, CONFIG : {LOG_SIZE : logSize}, OWNERID : ownerld})
    if obj_id == None:
    	return None
    else:
    	return obj_id
>>>>>>> master

def getServiceList(number, offset):
    return {}

#    def getNearTags(self, latitude, longitude):

<<<<<<< HEAD
def  getServiceIdByName(name):
    obj = db[COLLECTION].find_one({'name' : name})
    if obj != None:
        return obj
    raise ServiceNotFoundException()
=======
def getLog(dbName, number, offset, dateFrom, dateTo) :
	collection = db[COLLECTION_LOG_NAME]
	#if collection.count() == 0
	#	collection.drop()
	#	return None
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
>>>>>>> master
