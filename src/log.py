from db_model import addLogEntry
from config_reader import getDbName

# Log levels
LOG_LVL_INFO = 'info '
LOG_LVL_WARNING = 'warning'
LOG_LVL_ERROR = 'error'
LOG_LVL_CRITICAL = 'critical'


def writeInstanceLog(userId, message, level, service='instance'):
    addLogEntry(getDbName(), userId, message, level, service)


def writeServiceLog(serviceName, userId, message, level):
    addLogEntry(serviceName, userId, message, level)
