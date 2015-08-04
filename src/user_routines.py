from flask import session

from config_reader import getDbName
from db_model import getDbObject
from log import writeInstanceLog
from user_does_not_exist import UserDoesNotExist

USER_ID = 'user_id'
FIND_KEY_ID = "_id"
COLLECTION_NAME_USERS = "users"
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
EMAIL = 'email'
ANONYM_USER = 'anonym'

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

def addUser(_id, firstName, lastName, email):
    try:
        findUserById(_id)
    except UserDoesNotExist:
        collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]
        collectionUsers.insert({FIND_KEY_ID : _id, FIRST_NAME : firstName, LAST_NAME : lastName, EMAIL : email})
    finally:
        return _id

def getUserId():
    if USER_ID in session:
        return session[USER_ID]
    else:
        return ANONYM_USER
