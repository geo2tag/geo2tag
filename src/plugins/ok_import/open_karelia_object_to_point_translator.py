from datetime import datetime


class OpenKareliaObjectToPointTranslator:

    def __init__(
            self,
            serverShowImageUrl,
            serverShowObjectUrl,
            objectRepresentation,
            version,
            importSource,
            channelId):
        self.serverShowImageUrl = serverShowImageUrl
        self.serverShowObjectUrl = serverShowObjectUrl
        self.objectRepresentation = objectRepresentation
        self.version = version
        self.importSource = importSource
        self.channelId = channelId

    def getPointJson(self):
        obj = {}
        obj['name'] = self.objectRepresentation['name'][0]
        obj['image_url'] = self.serverShowImageUrl + \
            unicode(self.objectRepresentation.get('images', [{'$oid':''}])[0]['$oid'])
        obj['source_url'] = self.serverShowObjectUrl + \
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

        # Checking for intervals
        intervals_names = [['year_start', 'year_end'], ['century_start', 'century_end'],
                           ['millenium_start', 'millenium_end']]
        for i in range(3):
            if key_in_dict_and_defined(intervals_names[i][0], self.objectRepresentation) and \
                    key_in_dict_and_defined(intervals_names[i][1], self.objectRepresentation):
                bc = {'bc_start': None, 'bc_end': None}
                for i_bc in bc.keys():
                    if key_in_dict_and_defined(i_bc, self.objectRepresentation):
                        bc[i_bc] = self.objectRepresentation[i_bc]
                    else:
                        bc[i_bc] = False
                return date_name_to_datetime(self.objectRepresentation, intervals_names[i][0]), \
                    date_name_to_datetime(self.objectRepresentation, intervals_names[i][1]), \
                    bc['bc_start'], bc['bc_end']
        # Checking for precise dates
        date_names = ['year', 'century', 'millenium']
        for i in date_names:
            datetime_from_date_name = date_name_to_datetime(self.objectRepresentation, i)
            if datetime_from_date_name is not None:
                bc = None
                if key_in_dict_and_defined('bc', self.objectRepresentation):
                    bc = self.objectRepresentation['bc']
                else:
                    bc = False
                return datetime_from_date_name, bc
        return datetime.now(), False


# Defining date type to import from OK: precise date or interval
# then date adds to point dictionary
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

