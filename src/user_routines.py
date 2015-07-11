from flask import session

from config_reader import getDbName
from db_model import getDbObject
from log import writeInstanceLog
from user_does_not_exist import UserDoesNotExist

USER_ID = 'user_id'
COLLECTION_NAME_USERS = "users"

def logUserIn(_id):
    session[USER_ID] = _id
    writeInstanceLog(_id, 'login')

def logUserOut(_id):
    if USER_ID in session:
        session.pop(USER_ID)
    writeInstanceLog(_id, 'logout')

def findUserById(_id) :
    collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]
    userById = collectionUsers.find_one({USER_ID : _id})
    if userById != None :
        return userById
    raise UserDoesNotExist