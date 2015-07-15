import geojson

GEOJSON_SUPPORTED_TYPES = ['Point', 'Polygon', 'MultiPolygon']
GEOJSON_POLYGON_TYPES = ['Polygon', 'MultiPolygon']

GEOJSON_TYPE = 'type'
GEOJSON_COORDINATES = 'coordinates'

def GeoJsonType(obj):
    jsonObj = geojson.loads(obj)
    if (len(jsonObj.keys()) == 2) and \
       (GEOJSON_COORDINATES in jsonObj.keys()) and \
       (isinstance(jsonObj.get(GEOJSON_COORDINATES), list)):

        if jsonObj.get(GEOJSON_TYPE) in GEOJSON_SUPPORTED_TYPES:
            return jsonObj
        else:
            raise ValueError
    else:
        raise ValueError
