from db_model import addLogEntry
from config_reader import getDbName

def writeInstanceLog(userId, message,service): 
    addLogEntry(getMasterDbName(), userId, message, service)

def writeServiceLog(serviceName, userId, message): 
    addLogEntry(serviceName, userId, message)
