from pymongo import MongoClient
from log import writeInstanceLog
from config_reader import getDbName
from flask import session

#DB initialisation
client = MongoClient()
dbName = getDbName()

USER_ID = 'user_id'

def logUserIn(_id):
    session[USER_ID] = _id    
    writeInstanceLog(session[USER_ID], 'login')
def logUserOut():
    SESSION_VALUE = "Wasn't logged in"
    if USER_ID in session:
        SESSION_VALUE = session.pop(USER_ID)
    writeInstanceLog(SESSION_VALUE, 'logout')
