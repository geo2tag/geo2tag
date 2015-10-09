from json import dumps
import sys
sys.path.append('../../')
from db_model import getServiceIdByName, getChannelByName, getDbObject
sys.path.append('../../geocoders/')
from geocoder_request import GeonamesRequestSender
from geocoder_response_parser import GeocoderResponseParser

POINTS_COLL = 'points'
JSON = 'json'
ADDRESS = 'address'
ID = '_id'
PROC_BLOCK = 5000

def GeocoderImport(self,  channelName, serviceName):
    getServiceIdByName(serviceName)
    getChannelByName(serviceNamem, channelName)
    points_coll = getDbObject(serviceName)[POINTS_COLL]
    all_points = list(points_coll.find())
    greqv = GeonamesRequestSender()
    gpars = GeocoderResponseParser()
    point_blocks = slice_generator(all_points, PROC_BLOCK)
    for point_block in point_blocks:
        current_size = len(point_blocks)
        addresses = [point[JSON][ADDRESS] for point in point_block]
        ids = [point[ID] for point in point_block]
        string_addresses = greqv.requestCoordinates(addresses, 'geo2tag', json_list_to_list_of_strings)
        json_coords = gpars.parseList(string_addresses)
        for i in range(0, current_size):
            points_coll.update(
                {
                    ID: ids[i]
                },
                {
                    '$set': {
                        'location.coordinates': json_coords[i]
                    }
                }
            )

def json_list_to_list_of_strings(json_list):
    list_of_strings = []
    for json in json_list:
        list_of_strings.append(dumps(json))
    return list_of_strings

def slice_generator(list_for_slices, slice_size):
    slices = []
    for i in range(0, len(list_for_slices), slice_size):
        slices.append(list_for_slices[i:i+slice_size])
    return slices

def field_in_dict_and_defined(field, dictionary):
    return field in dictionary and dictionary[field] is not None

