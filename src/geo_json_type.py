import geojson

GEOJSON_SUPPORTED_TYPES = ['Point', 'Polygon', 'MultiPolygon']
GEOJSON_POLYGON_TYPES = ['Polygon', 'MultiPolygon']

GEOJSON_TYPE = 'type'
GEOJSON_COORDINATES = 'coordinates'


def GeoJsonType(obj):
    jsonObj = geojson.loads(obj)
    if (len(dict(jsonObj).keys()) == 2) and \
       (GEOJSON_COORDINATES in dict(jsonObj).keys()) and \
       (isinstance(dict(jsonObj).get(GEOJSON_COORDINATES), list)):

        if dict(jsonObj).get(GEOJSON_TYPE) in GEOJSON_SUPPORTED_TYPES:
            return jsonObj
        else:
            raise ValueError
    else:
        raise ValueError
