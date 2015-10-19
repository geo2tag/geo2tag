from json import dumps
from db_model import getServiceIdByName, getChannelByName, getDbObject
from config_reader import getGeonamesLogin
from geocoder_request import GeonamesRequestSender
from geocoder_response_parser import GeocoderResponseParser

POINTS_COLL = 'points'
CHANNEL_ID = 'channel_id'
JSON = 'json'
ADDRESS = 'address'
ID = '_id'
PROC_BLOCK = 5000


def geocoderImport(self,  channelName, serviceName):
    # Checking for service existence
    getServiceIdByName(serviceName)
    # Getting channel id
    channel = getChannelByName(serviceName, channelName)
    channel_id = channel[ID]
    # Initialising requester and parser
    greqv = GeonamesRequestSender()
    gpars = GeocoderResponseParser()
    # Getting points collection
    points_coll = getDbObject(serviceName)[POINTS_COLL]
    # Getting first slice of <= 5000 points
    proc_step = 0
    point_block = list(points_coll.find({
        CHANNEL_ID: channel_id,
        JSON+'.'+ADDRESS: {"$exists": True}
    }).skip(proc_step).limit(PROC_BLOCK))
    while point_block:
        current_size = len(point_block)
        addresses = [point[JSON][ADDRESS] for point in point_block]
        ids = [point[ID] for point in point_block]
        string_addresses = greqv.requestCoordinates(
            addresses,
            getGeonamesLogin(),
            json_list_to_list_of_strings)
        json_coords = gpars.parseList(string_addresses)
        for i in range(0, current_size):
            # If no coords was found - we change nothing
            if json_coords[i] is None:
                continue
            points_coll.update(
                {ID: ids[i]},
                {'$set': {'location.coordinates': json_coords[i]}}
            )
        # Getting next slice of <= 5000 points
        proc_step += PROC_BLOCK
        point_block = list(points_coll.find().skip(proc_step).limit(PROC_BLOCK))


def json_list_to_list_of_strings(json_list):
    list_of_strings = []
    for json in json_list:
        list_of_strings.append(dumps(json))
    return list_of_strings


def field_in_dict_and_defined(field, dictionary):
    return field in dictionary and dictionary[field] is not None
