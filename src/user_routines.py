from flask import session
from config_reader import getDbName
from db_model import getDbObject
from log import writeInstanceLog
from log import LOG_LVL_INFO
from user_does_not_exist import UserDoesNotExist

USER_ID = 'user_id'
USER_LOGIN = 'user_login'
FIND_KEY_ID = "_id"
COLLECTION_NAME_USERS = "users"
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
EMAIL = 'email'
ANONYM_USER = 'anonym'
ANONYM = 'Anonym'
LOGIN = 'login'
LOGOUT = 'logout'


def logUserIn(_id, user_login=None):
    session[USER_ID] = _id
    if user_login is not None:
        session[USER_LOGIN] = user_login
    writeInstanceLog(session[USER_ID], LOGIN, LOG_LVL_INFO)


def logUserOut():
    if USER_ID in session:
        SESSION_VALUE = session.pop(USER_ID)
        writeInstanceLog(SESSION_VALUE, LOGOUT, LOG_LVL_INFO)


def findUserById(_id):
    collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]
    userById = collectionUsers.find_one({FIND_KEY_ID: _id})
    if userById is not None:
        return userById
    raise UserDoesNotExist


def addUser(_id, firstName, lastName, email):
    return_id = _id
    try:
        findUserById(_id)
    except UserDoesNotExist:
        collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]
        collectionUsers.insert(
            {FIND_KEY_ID: _id, FIRST_NAME: firstName, LAST_NAME: lastName,
             EMAIL: email})
    finally:
        return_id = _id
    return return_id


def getUserId():
    try:
        return session[USER_ID]
    except Exception:
        return ANONYM_USER


def findUsers(number, offset, loginSubstring):
    collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]
    result = list(collectionUsers.find(
        {LOGIN: {'$regex': ".*" + loginSubstring + ".*"}}).skip(
            offset).limit(number))
    return result
