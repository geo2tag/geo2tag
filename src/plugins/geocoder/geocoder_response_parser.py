from json import loads
TOTAL_RESULTS_COUNT = 'totalResultsCount'
GEONAMES = 'geonames'
LAT = 'lat'
LNG = 'lng'


class GeocoderResponseParser():

    @classmethod
    def parseSingle(cls, text):
        # in return:
        # 1) None - if no lat or lng vars was found
        # 2) [lat, lan]]
        JSONconv = loads(text)
        resArr = None
        if field_in_dict_and_defined(TOTAL_RESULTS_COUNT, JSONconv) and JSONconv[TOTAL_RESULTS_COUNT] == 0:
            return None
        if field_in_dict_and_defined(GEONAMES, JSONconv):
            resArr = [
                float(JSONconv[GEONAMES][0][LNG]),
                float(JSONconv[GEONAMES][0][LAT])
            ]
        return resArr

    @classmethod
    def parseList(cls, textList):
        # in return
        # 1) None - if every response has no lat & lng
        # 2) list of [lng, lat]
        JSONres = []
        for i in textList:
            JSONsingle = cls.parseSingle(i)
            JSONres.append(JSONsingle)
        if len(JSONres) == 0:
            return None
        return JSONres


def field_in_dict_and_defined(field, dictionary):
    return field in dictionary and dictionary[field] is not None
