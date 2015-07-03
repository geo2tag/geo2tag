from pymongo import MongoClient
from log import writeInstanceLog
from config_reader import getDbName

# Collection
SESSION = 'session'

#DB initialisation
client = MongoClient()
dbName = getDbName()
collection = client[dbName][SESSION]

def logUserIn(_id):
    collection.save({'user_id' : _id})
    writeInstanceLog(_id, 'login')

def logUserOut(_id):
    collection.remove({'user_id' : _id})
    writeInstanceLog(_id, 'logout')
