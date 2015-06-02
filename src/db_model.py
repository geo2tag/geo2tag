from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
from  service_not_found_exception import ServiceNotFoundException
from pymongo import Connection

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
    obj_id = db[COLLECTION].save({NAME : name, CONFIG : {LOG_SIZE : logSize}, OWNERID : ownerld})
    if obj_id == None:
    	return None
    else:
    	return obj_id

def getServiceList(number, offset):
    return {}

def getServiceIdByName(name):
    obj = db[COLLECTION].find_one({'name' : name})
    if obj != None:
        return obj
    raise ServiceNotFoundException()

def removeService(name):
    obj = db[COLLECTION].remove({NAME : name})
    connection = Connection()
    connection.drop_database(name)