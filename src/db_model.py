from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
import pymongo
from datetime import datetime
from  service_not_found_exception import ServiceNotFoundException
from pymongo import Connection

# getLog constants
COLLECTION_LOG_NAME = "log"
FIND_AND_SORT_KEY = "date"

#updateService constants
COLLECTION_SERVICES_NAME = "services"
COLLECTION_SERVICES_EL_CONFIG_NAME = "config"

# Collections
TAGS = 'tags'
COLLECTION = 'services'
NAME = 'name'
CONFIG = 'config'
LOG_SIZE = 'log_size'
OWNERID = 'owner_id'
ID = '_id'

#db initialisation
db = MongoClient(getHost(), getPort())[getDbName()]

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

def updateService(name, config) :
    services_collection = db[COLLECTION_SERVICES_NAME]
    for el in config :
        tmp_el_to_set = COLLECTION_SERVICES_EL_CONFIG_NAME + '.' + str(el)
        services_collection.update(
            {"name" : name},
            #changes will affect on service's sub-document called 'config'
            #if there is no such sub-document called 'config', it will be created
            {"$set" : {tmp_el_to_set : config[el]}},
            #changes will affect on all services with name mentioned above
            multi = True
        )
    #changed service(s) cursor in return
    return services_collection.find({"name" : name})

def  getServiceIdByName(name):
    obj = db[COLLECTION].find_one({NAME : name})
    if obj != None:
        return obj
    raise ServiceNotFoundException()

def removeService(name):
    try:
        obj = getServiceIdByName(name)
        db[COLLECTION].remove({ID : obj['_id']})
        connection = Connection()
        connection.drop_database(name)
    except ServiceNotFoundException as e:
        raise

def  getServiceById(id):
    obj = db[COLLECTION].find_one({ID : id})
    if obj != None:
        return obj
    raise ServiceNotFoundException()