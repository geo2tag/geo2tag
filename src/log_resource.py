import pymongo
from pymongo import MongoClient
import datetime
from datetime import datetime
import json
from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse


class LogResource(Resource):
    def get(self, serviceName = None):
    	parser_dict = parse()
    	if serviceName == None:
    		serviceName = 'masterDbName'

    	return getLog(serviceName, parser_dict['number'], parser_dict['offset'], 
    		parser_dict['dateFrom'], parser_dict['dateTo'])

def getLog(dbName, number = 0, offset = 0, dateFrom = datetime.today(), dateTo = datetime.today()) :
	log = []
	client = MongoClient()
	db = client[dbName]
	collection = db["log"]
	for el in collection.find({"date" : {"$gte" : dateFrom , "$lte" : dateTo}}, None, int(offset), int(number)).sort("date", pymongo.ASCENDING) :
		log.append(el)
	return log
def parse():
    parser = reqparse.RequestParser()
    parser.add_argument('number', type=int, default=None)
    parser.add_argument('offset', type=int, default=None)
    parser.add_argument('date_from', type=datetime, default=None)
    parser.add_argument('date_to', type=datetime, default=None)
    args = parser.parse_args()
    return args