from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName

# Collections
TAGS = 'tags'
db = MongoClient(getHost(), getPort())[getDbName()]

def addTag(tag):
    db[TAGS].insert(tag)

#    def getNearTags(self, latitude, longitude):