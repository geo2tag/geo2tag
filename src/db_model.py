from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
import pymongo
from datetime import datetime

COLL_LOG = "log"

# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]

def addTag(tag):
    db[TAGS].insert(tag)

#    def getNearTags(self, latitude, longitude):

def getLog(dbName, number, offset, dateFrom, dateTo) :
	collection = db[COLL_LOG]
	if number == None :
		number = 0
	if offset == None :
		offset = 0
	if dateFrom == None && dateTo == None :
		return None
	elif dateFrom == None :
		return collection.find({"date" : {"$lte" : dateTo}}, None, offset, number).sort("date", pymongo.ASCENDING)	
	elif dateTo == None :
		return collection.find({"date" : {"$gte" : dateFrom}}, None, offset, number).sort("date", pymongo.ASCENDING)
	else 
		return collection.find({"date" : {"$gte" : dateFrom , "$lte" : dateTo}}, None, offset, number).sort("date", pymongo.ASCENDING)

