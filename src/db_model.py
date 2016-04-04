from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
import pymongo
from datetime import datetime
from service_not_exist_exception import ServiceNotExistException
from service_already_exists_exception import ServiceAlreadyExistsException
from pymongo import Connection
from bson.objectid import ObjectId
from channel_does_not_exist import ChannelDoesNotExist
from point_does_not_exist import PointDoesNotExist
from geo_json_type import GEOJSON_TYPE, GEOJSON_POLYGON_TYPES, \
    GEOJSON_COORDINATES
from metadata_does_not_exist_exception import MetadataDoesNotExistException

# getLog constants
COLLECTION_LOG_NAME = "log"
FIND_AND_SORT_KEY = "date"

# getPointById constants
COLLECTION_POINTS_NAME = "points"
POINTS_FIND_AND_KEY = "_id"

# updateService constants
COLLECTION_SERVICES_NAME = "services"
COLLECTION_SERVICES_EL_CONFIG_NAME = "config"

# Collections
TAGS = 'tags'
COLLECTION = 'services'
NAME = 'name'
CONFIG = 'config'
LOG_SIZE = 'log_size'
OWNERID = 'owner_id'
ID = '_id'
LOG = 'log'
BC = 'bc'
METADATA = 'metadata'

# db initialisation
MONGO_CLIENT = None  # MongoClient(getHost(), getPort())

db = MongoClient(getHost(), getPort())[getDbName()]
# keys
USER_ID = 'user_id'
DATE = 'date'
MESSAGE = 'message'
LEVEL = 'level'
ERROR_CODE = 'error_code'
SERVICE = 'service'
COLLECTION = 'services'
CHANNELS_COLLECTION = 'channels'
POINTS_COLLECTION = 'points'
JSON = 'json'
ACL = 'acl'
OWNER_GROUP = 'owner_group'
POINTS_COLLECTION = 'points'
LOCATION = 'location'
TYPE = 'type'
POINT = 'Point'
COORDINATES = 'coordinates'
LON = 'lon'
LAT = 'lat'
ALT = 'alt'
CHANNEL_ID = 'channel_id'
PLUGINS = 'plugins'
ENABLED = 'enabled'
CONFIGURABLE = 'configurable'

EARTH_RADIUS = 6371


def addLogEntry(dbName, userId, message, level, service='instance'):
    currentDate = datetime.now()
    collection = getDbObject(dbName)[LOG]
    if dbName == getDbName():
        collection.save({USER_ID: userId, DATE: currentDate,
                         MESSAGE: message, LEVEL: level, SERVICE: service})
    else:
        collection.save({
            USER_ID: userId,
            DATE: currentDate,
            MESSAGE: message,
            LEVEL: level
        })


def addTag(tag):
    getDbObject()[TAGS].insert(tag)


def addService(name, logSize, ownerld):
    db_addservice = getDbObject()
    try:
        getServiceIdByName(name)
        raise ServiceAlreadyExistsException()
    except ServiceNotExistException:
        obj_id = db_addservice[COLLECTION].save(
            {NAME: name, CONFIG: {LOG_SIZE: logSize}, OWNERID: ownerld})
        addServiceDb(name)
        if obj_id is None:
            return None
        else:
            return obj_id


def getLog(dbName, number, offset, dateFrom, dateTo):
    dbLog = getDbObject(dbName)
    criterion = {}
    number = 0 if (number is None or number < 0) else number
    offset = 0 if (offset is None or offset < 0) else offset
    dateFrom = datetime(2000, 1, 1, 0, 0) if (dateFrom is None) else dateFrom
    dateTo = datetime.now() if (dateTo is None) else dateTo
    if dateFrom > dateTo:
        return []
    applyDateCriterion(DATE, dateFrom, False, dateTo, False, criterion)
    criterion.pop('bc', None)
    return dbLog[COLLECTION_LOG_NAME].find(
        criterion, None, offset, number).sort(DATE, pymongo.DESCENDING)


def updateService(name, config):
    services_collection = db[COLLECTION_SERVICES_NAME]
    for el in config:
        tmp_el_to_set = COLLECTION_SERVICES_EL_CONFIG_NAME + '.' + unicode(el)
        services_collection.update(
            {"name": name},
            # changes will affect on service's sub-document called 'config'
            # if there is no such sub-document called 'config', it will be
            # created
            {"$set": {tmp_el_to_set: config[el]}},
            # changes will affect on all services with name mentioned above
            multi=True
        )
    # changed service(s) cursor in return
    return services_collection.find({"name": name})


def getServiceIdByName(name):
    obj = getDbObject()[COLLECTION].find_one({NAME: name})
    print obj
    if obj is not None:
        return obj
    raise ServiceNotExistException()


def removeService(name):
    try:
        obj = getServiceIdByName(name)
        db[COLLECTION].remove({ID: obj['_id']})
        connection = Connection()
        connection.drop_database(name)
    except ServiceNotExistException:
        raise


def getServiceById(id_service):
    obj = getDbObject()[COLLECTION].find_one({ID: id_service})
    if obj is not None:
        return obj
    raise ServiceNotExistException()


def getServiceList(number, offset, serviceSubstr, ownerId):
    db_getservicelist = getDbObject()
    criterion = {}
    collection = db_getservicelist[COLLECTION]
    if number is None:
        number = collection.count()
    if serviceSubstr is not None:
        criterion['name'] = {'$regex': serviceSubstr}
    if ownerId:
        criterion['owner_id'] = ownerId
    print 'getServiceList(number, offset, serviceSubstr, ownerId):'
    print criterion
    coursor = collection.find(criterion)
    return list(coursor.sort(NAME, 1).skip(offset).limit(number))


def getChannelsList(serviceName, substring, number, offset):
    db_getchannellist = getDbObject(serviceName)
    if substring is not None and number is not None and offset is not None:
        return db_getchannellist[CHANNELS_COLLECTION].find(
            {'name': {'$regex': substring}}).skip(offset).limit(number)
    elif substring is not None and offset is not None:
        return db_getchannellist[CHANNELS_COLLECTION].find(
            {'name': {'$regex': substring}}).skip(offset)
    elif substring is not None and number is not None:
        return db_getchannellist[CHANNELS_COLLECTION].find(
            {'name': {'$regex': substring}}).limit(number)
    elif offset is not None and number is not None:
        return db_getchannellist[
            CHANNELS_COLLECTION].find().skip(offset).limit(number)
    elif substring is not None:
        return db_getchannellist[CHANNELS_COLLECTION].find(
            {'name': {'$regex': substring}})
    elif number is not None:
        return db_getchannellist[CHANNELS_COLLECTION].find().limit(number)
    elif offset is not None:
        return db_getchannellist[CHANNELS_COLLECTION].find().skip(offset)


def getChannelById(serviceName, channelId):
    db_channelbyid = getDbObject(serviceName)
    if isinstance(channelId, str) or isinstance(channelId, unicode):
        obj = db_channelbyid[CHANNELS_COLLECTION].find_one(
            {'_id': ObjectId(channelId)})
    else:
        obj = db_channelbyid[CHANNELS_COLLECTION].find_one({'_id': channelId})
    if obj is not None:
        return obj
    raise ChannelDoesNotExist()


def getDbObject(dbName=getDbName()):
    return getClientObject()[dbName]


def getClientObject():
    global MONGO_CLIENT
    if MONGO_CLIENT is None:
        MONGO_CLIENT = MongoClient(getHost(), getPort())
#    print "getClientObject: {0}".format(hex(id(MONGO_CLIENT)))
    return MONGO_CLIENT


def deleteChannelById(serviceName, channelId):
    db_deletechannlebyid = getDbObject(serviceName)
    if isinstance(channelId, str) or isinstance(channelId, unicode):
        result = list(db_deletechannlebyid[CHANNELS_COLLECTION].find(
            {'_id': ObjectId(channelId)}))
    else:
        result = list(db_deletechannlebyid[
                      CHANNELS_COLLECTION].find({'_id': channelId}))
    if len(result) > 0:
        db_deletechannlebyid[CHANNELS_COLLECTION].remove(
            {'_id': ObjectId(channelId)})
    else:
        raise ChannelDoesNotExist()


def addChannel(name, json, owner_id, serviceName):
    db_addchannel = getDbObject(serviceName)
    return db_addchannel[CHANNELS_COLLECTION].insert(
        {NAME: name, JSON: json, OWNERID: owner_id, OWNER_GROUP: 'STUB',
         ACL: 777})


def updateChannel(serviceName, channelId, name, json, acl):
    db_updatechannel = getDbObject(serviceName)
    try:
        obj = db_updatechannel[CHANNELS_COLLECTION].find_one(
            {ID: ObjectId(channelId)})
    except:
        raise ChannelDoesNotExist()
    if obj is None:
        raise ChannelDoesNotExist()
    else:
        obj['name'] = name
        if json is not None:
            obj['json'] = json
        if acl is not None:
            obj['acl'] = acl
        db_updatechannel[CHANNELS_COLLECTION].save(obj)


def getChannelByName(serviceName, channelName):
    db_getchannelbyname = getDbObject(serviceName)
    obj = db_getchannelbyname[
        CHANNELS_COLLECTION].find_one({NAME: channelName})
    if obj is not None:
        return obj
    raise ChannelDoesNotExist()


def deletePointById(serviceName, pointId):
    db_deletepointbyid = getDbObject(serviceName)
    obj = db_deletepointbyid[POINTS_COLLECTION].find_one(
        {ID: ObjectId(pointId)})
    if obj is not None:
        db_deletepointbyid[POINTS_COLLECTION].remove({ID: ObjectId(pointId)})
    else:
        raise PointDoesNotExist()


def getPointById(serviceName, pointId):
    pointsCollection = getDbObject(serviceName)[COLLECTION_POINTS_NAME]
    point = pointsCollection.find_one(
        {POINTS_FIND_AND_KEY: ObjectId(unicode(pointId))})
    if point is not None:
        return point
    raise PointDoesNotExist()


def addPoints(serviceName, pointsArray):
    db_addpoint = getDbObject(serviceName)[COLLECTION_POINTS_NAME]
    list_id = []
    for point in pointsArray:
        obj = {}
        obj[JSON] = point[JSON]
        obj[LOCATION] = {TYPE: POINT, COORDINATES: [point[LON], point[LAT]]}
        obj[ALT] = point[ALT]
        obj[CHANNEL_ID] = ObjectId(point[CHANNEL_ID])
        obj[DATE] = datetime.now()
        obj[BC] = point[BC]
        list_id.append(unicode(db_addpoint.save(obj)))
    return list_id


def updatePoint(serviceName, pointId, changes):
    db_updatepoint = getDbObject(serviceName)
    try:
        obj = db_updatepoint[POINTS_COLLECTION].find_one(
            {ID: ObjectId(pointId)})
    except:
        raise PointDoesNotExist()
    if obj is None:
        raise PointDoesNotExist()
    else:
        for key in changes.keys():
            if key in obj.keys():
                obj[key] = changes[key]
        db_updatepoint[POINTS_COLLECTION].save(obj)
    print obj


def addServiceDb(dbName):
    db_addservicedb = getDbObject(dbName)
    pymongo.GEOSPHERE = '2dsphere'
    pymongo.DESCENDING = -1
    db_addservicedb[COLLECTION_POINTS_NAME].ensure_index(
        [("location", pymongo.GEOSPHERE)])
    db_addservicedb[COLLECTION_POINTS_NAME].create_index(
        [("date", pymongo.DESCENDING)])
    db_addservicedb[COLLECTION_POINTS_NAME].create_index(
        [("name", pymongo.ASCENDING)])


def applyFromToCriterion(field, value_from, value_to, criterion):
    if value_from or value_to:
        fieldCriterion = {}
        if value_from:
            fieldCriterion['$gte'] = value_from
        if value_to:
            fieldCriterion['$lte'] = value_to
        criterion[field] = fieldCriterion


def applyDateCriterion(field, date_from, bc_from, date_to, bc_to, criterion):
    fieldCriterion = {}
    if date_from and bc_from and date_to and not(bc_to):
        criterion['$or'] = [{'date': {'$lte': date_from}, 'bc': True}, {
            'date': {'$lte': date_to}, 'bc': False}]
        return
    if date_from and bc_from and date_to and bc_to:
        fieldCriterion['$lte'] = date_from
        fieldCriterion['$gte'] = date_to
        criterion[field] = fieldCriterion
        criterion['bc'] = True
        return
    if date_from and not(bc_from) and date_to and not(bc_to):
        fieldCriterion['$gte'] = date_from
        fieldCriterion['$lte'] = date_to
        criterion[field] = fieldCriterion
        criterion['bc'] = False
        return
    if date_from is None and date_to and not(bc_to):
        criterion['$or'] = [
            {'bc': True}, {'date': {'$lte': date_to}, 'bc': False}]
        return
    if date_from and not(bc_from) and date_to is None:
        fieldCriterion['$gte'] = date_from
        criterion['bc'] = False
        criterion[field] = fieldCriterion
        return
    if date_from is None and bc_to and date_to:
        fieldCriterion['$gte'] = date_to
        criterion['bc'] = True
        criterion[field] = fieldCriterion
        return
    if date_from and bc_from and date_to is None:
        criterion['$or'] = [
            {'bc': False}, {'date': {'$lte': date_from}, 'bc': True}]
        return


def applyGeometryCriterion(geometry, radius, criterion):
    if geometry:
        locationCriterion = {}
        if geometry[GEOJSON_TYPE] in GEOJSON_POLYGON_TYPES:
            # Filter as polygon
            locationCriterion = {'$geometry': geometry}
        else:
            # Filter as cirlce
            longitude = geometry[GEOJSON_COORDINATES][0]
            latitude = geometry[GEOJSON_COORDINATES][1]
            locationCriterion = {'$centerSphere': [
                [longitude, latitude], radius / EARTH_RADIUS]}
        criterion[LOCATION] = {'$geoWithin': locationCriterion}

# Substring is skipped


def findPoints(
        serviceName,
        channel_ids,
        number,
        geometry=None,
        altitude_from=None,
        altitude_to=None,
        _=None,
        date_from=None,
        date_to=None,
        offset=None,
        radius=1000,
        bc_from=False,
        bc_to=False
):
    db_findepoint = getDbObject(serviceName)

    # Converting types
    channel_ids = [ObjectId(channel_id) for channel_id in channel_ids]
    criterion = {CHANNEL_ID: {'$in': channel_ids}}

    # applyFromToCriterion(DATE, date_from, date_to, criterion)
    applyFromToCriterion(ALT, altitude_from, altitude_to, criterion)

    applyGeometryCriterion(geometry, radius, criterion)
    applyDateCriterion(DATE, date_from, bc_from, date_to, bc_to, criterion)
    points = db_findepoint[POINTS_COLLECTION].find(
        criterion).sort(DATE, pymongo.DESCENDING)
    if offset:
        points.skip(offset)
    points.limit(number)
    return points


def closeConnection():
    if MONGO_CLIENT is not None:
        MONGO_CLIENT.close()


def getPluginInfo(pluginName):
    db_getpluginstate = getDbObject()
    obj = db_getpluginstate[PLUGINS].find_one({NAME: pluginName})
    plugin_state = {ENABLED: False, CONFIGURABLE: True}
    if obj is not None:
        if CONFIGURABLE in obj:
            plugin_state = {ENABLED: obj[ENABLED], CONFIGURABLE:
                            obj[CONFIGURABLE]}
        else:
            plugin_state = {ENABLED: obj[ENABLED], CONFIGURABLE: True}
    return plugin_state


def getPluginState(pluginName):
    db_getpluginstate = getDbObject()
    obj = db_getpluginstate[PLUGINS].find_one({NAME: pluginName})
    if obj is not None:
        return obj[ENABLED]
    else:
        return False


def setPluginState(pluginName, state):
    if isinstance(state, str) or isinstance(state, unicode):
        if state.lower() == 'true':
            state = True
        else:
            state = False

    db_setplugin = getDbObject()
    obj = db_setplugin[PLUGINS].find_one({NAME: pluginName})
    if obj is None:
        db_setplugin[PLUGINS].save({NAME: pluginName, ENABLED: state})
    else:
        obj[ENABLED] = state
        db_setplugin[PLUGINS].save(obj)


def getAllChannelIds(serviceName):
    all_channel_ids_array = []
    db_getallchanelids = getDbObject(serviceName)
    obj = db_getallchanelids[CHANNELS_COLLECTION].find()
    for result in obj:
        all_channel_ids_array.append(unicode(result[ID]))
    return all_channel_ids_array


def setMetadata(serviceName, data, _id=None):
    obj = data
    if _id is not None:
        obj[ID] = ObjectId(_id)
    db_set_metadata = getDbObject(serviceName)
    return db_set_metadata[METADATA].save(obj)


def deleteMetadataById(serviceName, _id):
    collection = getDbObject(serviceName)[METADATA]
    getMetadataById(serviceName, _id)
    collection.remove({ID: ObjectId(unicode(_id))})


def getMetadataById(serviceName, _id):
    obj = getDbObject(serviceName)[METADATA].find_one(
        {ID: ObjectId(unicode(_id))})
    if obj is not None:
        return obj
    raise MetadataDoesNotExistException()


def findMetadata(serviceName, number, offset, queryPairs):
    collection = getDbObject(serviceName)[METADATA]
    criterion = {}
    if queryPairs and isinstance(queryPairs, dict):
        criterion = queryPairs
    metadataElements = collection.find(criterion)
    metadataElements.skip(offset)
    metadataElements.limit(number)
    return metadataElements
