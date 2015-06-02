from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
import pymongo
from datetime import datetime

# getLog constants
COLLECTION_LOG_NAME = "log"
FIND_AND_SORT_KEY = "date"

# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]

def addTag(tag):
    db[TAGS].insert(tag)

#    def getNearTags(self, latitude, longitude):

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

