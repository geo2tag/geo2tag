import pymongo
from pymongo import MongoClient
import datetime
from datetime import datetime
import json

def getLog(dbName, number = 0, offset = 0, dateFrom = datetime.today(), dateTo = datetime.today()) :
	log = []
	client = MongoClient()
	db = client[dbName]
	collection = db["log"]
	for el in collection.find({"date" : {"$gte" : dateFrom , "$lte" : dateTo}}, None, int(offset), int(number)).sort("date", pymongo.ASCENDING) :
		log.append(el)
	return log
