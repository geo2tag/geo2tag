from datetime import datetime
import sys
sys.path.append('../../open_data_import')
from open_data_object_to_point_translator import OpenDataToPointTranslator

INTERVAL_DATES_NAMES = (('year_start', 'year_end'), ('century_start', 'century_end'),
                           ('millenium_start', 'millenium_end'))
PRECISE_DATE_NAMES = ('year', 'century', 'millenium')
DATE_TYPES = ('interval', 'precise')

class OpenKareliaObjectToPointTranslator(OpenDataToPointTranslator):

    def __init__(
            self,importDataDict,
            objectRepresentation,
            version,
            importSource,
            channelId):
        super(OpenKareliaObjectToPointTranslator, self).__init__(importDataDict,
            objectRepresentation,
            version,
            importSource,
            channelId)

    def getPointJson(self):
        obj = {}
        obj['name'] = self.objectRepresentation['name'][0]
        obj['image_url'] = self.importDataDict['image_url'] + \
            unicode(self.objectRepresentation.get('images', [{'$oid': ''}])[0]['$oid'])
        obj['source_url'] = self.importDataDict['image_url'] + \
            unicode(self.objectRepresentation.get('_id'))
        obj['version'] = self.version
        obj['import_source'] = self.importSource
        return obj

    def getPoint(self):
        point = {'json': self.getPointJson()}
        point['channel_id'] = self.channelId
        point['location'] = {
            "type": "Point",
            "coordinates": [
                float(self.objectRepresentation['latitude']),
                float(self.objectRepresentation['longitude'])]}
        point['alt'] = 0
        # Date trnslation
        trans_date = self.translateDate()
        print trans_date
        add_precise_or_interval_to_point(trans_date, point)
        return point

    def translateDate(self):
        # Return values are tuples:
        # 1) Interval of dates and bc types of both dates
        # 2) Precise date and bc type of date
        # Examples:
        # 1) Intervals:
        #    datetime.datetime(1000, 1, 1, 0, 0),
        #    datetime.datetime(2000, 1, 1, 0, 0),
        #    False,
        #    False
        # 1) Precise date:
        #    datetime.datetime(1000, 1, 1, 0, 0),
        #    False

        date_type = define_date_type(self.objectRepresentation)

        if date_type is None:
            # if no full intervals and no precise dates
            return datetime.now(), False  
        elif date_type[0] == DATE_TYPES[0]:
            # Checking for intervals
            bc = {'bc_start': False, 'bc_end': False}
            for i_bc in bc.keys():
                if key_in_dict_and_defined(i_bc, self.objectRepresentation):
                    bc[i_bc] = self.objectRepresentation[i_bc]
            return date_name_to_datetime(self.objectRepresentation, INTERVAL_DATES_NAMES[date_type[1]][0]), \
                date_name_to_datetime(self.objectRepresentation, INTERVAL_DATES_NAMES[date_type[1]][1]), \
                bc['bc_start'], bc['bc_end']
        elif date_type[0] == DATE_TYPES[1]:
            # Checking for precise dates
            datetime_from_date_name = date_name_to_datetime(self.objectRepresentation, PRECISE_DATE_NAMES[date_type[1]])
            bc = False
            if key_in_dict_and_defined('bc', self.objectRepresentation):
                bc = self.objectRepresentation['bc']
            return datetime_from_date_name, bc

# Defining date type to import from OK
def define_date_type(objectRepresentation):
    # Return values are tuples:
    # 1) 'interval', INTERVAL_SCALE
    # 2) 'precise', PRECISE_SCALE
    # 3) Default value - None
    # !) SCALE is: year*, century*, millenium*
    for i in range(len(INTERVAL_DATES_NAMES)):
        if key_in_dict_and_defined(INTERVAL_DATES_NAMES[i][0], objectRepresentation) and \
                    key_in_dict_and_defined(INTERVAL_DATES_NAMES[i][1], objectRepresentation):
            return DATE_TYPES[0], i
    for i in range(len(PRECISE_DATE_NAMES)):
        if key_in_dict_and_defined(PRECISE_DATE_NAMES[i], objectRepresentation):
            return DATE_TYPES[1], i
    return None

# Adding dates to point dictionary
def add_precise_or_interval_to_point(precise_or_interval_list, point):
    if len(precise_or_interval_list) == 2:
        point['date'] = precise_or_interval_list[0]
        point['bc'] = precise_or_interval_list[1]
    else:
        point['date'] = precise_or_interval_list[0]
        point['json']['date'] = precise_or_interval_list[1]
        point['bc'] = precise_or_interval_list[2]
        point['json']['bc'] = precise_or_interval_list[3]


def key_in_dict_and_defined(key, dictionary):
    return key in dictionary and dictionary[key] is not None


# Date names translation to datetime format, for example year 1000 to
# datetime.datetime(1000, 1, 1, 0, 0)
def date_name_to_datetime(names_dict, names_key):
    if key_in_dict_and_defined(names_key,names_dict):
        if names_key == 'year' or names_key == 'year_start' or names_key == 'year_end':
            return datetime(int(names_dict[names_key]), 1, 1, 0, 0)
        elif names_key == 'century' or names_key == 'century_start' or names_key == 'century_end':
            return datetime(int(names_dict[names_key]) * 100, 1, 1, 0, 0)
        elif names_key == 'millenium' or names_key == 'millenium_start' or names_key == 'millenium_end':
            return datetime(int(names_dict[names_key]) * 1000, 1, 1, 0, 0)
    return None
