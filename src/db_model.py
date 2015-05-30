from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
from  service_not_found_exception import ServiceNotFoundException

# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]
COLLECTION = 'services'

def addTag(tag):
    db[TAGS].insert(tag)

def addService(name, logSize, ownerld):
    obj = db[COLLECTION].find_one({'name' : name})
    if obj != None:
        return False
    db[COLLECTION].save({'name' : name, 'config' : {'log_size' : logSize}, 'owner_id' : ownerld})
    obj = db[COLLECTION].find_one({'name' : name})
    if obj == None:
    	return None
    else:
    	return obj['_id']

#    def getNearTags(self, latitude, longitude):

def  getServiceIdByName(name):
    obj = db[COLLECTION].find_one({'name' : name})
    if obj != None:
        return obj
    ServiceExceprion = ServiceNotFoundException(NameError)
    return ServiceExceprion.getReturnObject()