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
    writeInstanceLog(_id, 'login')

def logUserOut(_id):
    if USER_ID in session:
        session.pop(USER_ID)
    writeInstanceLog(_id, 'logout')
