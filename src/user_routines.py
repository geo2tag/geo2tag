from flask import session

from config_reader import getDbName
from db_model import getDbObject
from log import writeInstanceLog
from user_does_not_exist import UserDoesNotExist

USER_ID = 'user_id'
FIND_KEY_ID = "_id"
COLLECTION_NAME_USERS = "users"

def logUserIn(_id):
    session[USER_ID] = _id    
    writeInstanceLog(session[USER_ID], 'login')

def logUserOut():
    if USER_ID in session:
        SESSION_VALUE = session.pop(USER_ID)
        writeInstanceLog(SESSION_VALUE, 'logout')

def findUserById(_id) :
    collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]
    userById = collectionUsers.find_one({FIND_KEY_ID : _id})
    if userById != None :
        return userById
    raise UserDoesNotExist
