from json import loads
TOTAL_RESULTS_COUNT = 'totalResultsCount'
GEONAMES = 'geonames'
LAT = 'lat'
LNG = 'lng'


class GeocoderResponseParser():

    @classmethod
    def parseSingle(cls, text):
        JSONconv = loads(text)
        resArr = list()
        if field_in_dict_and_defined(TOTAL_RESULTS_COUNT, JSONconv) and JSONconv[TOTAL_RESULTS_COUNT] == 0:
            return None
        if field_in_dict_and_defined(GEONAMES, JSONconv):
            for i in JSONconv[GEONAMES]:
                if field_in_dict_and_defined(LAT, i) and field_in_dict_and_defined(LNG, i):
                    resArr.append([float(i[LAT]), float(i[LNG])])
        if len(resArr) == 0:
            return None
        return resArr

    @classmethod
    def parseList(cls, textList):
        JSONres = list()
        for i in textList:
            JSONsingle = cls.parseSingle(i)
            if JSONsingle is not None:
                JSONres += JSONsingle
        if len(JSONres) == 0:
            return None
        return JSONres


def field_in_dict_and_defined(field, dictionary):
    return field in dictionary and dictionary[field] is not None
