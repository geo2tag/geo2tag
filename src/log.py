from db_model import addLogEntry
from config_reader import getDbName


def writeInstanceLog(userId, message, error_code, service='instance'):
    addLogEntry(getDbName(), userId, message, error_code, service)


def writeServiceLog(serviceName, userId, message):
    addLogEntry(serviceName, userId, message)
