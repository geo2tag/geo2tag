import geojson

def GeoJsonType(obj):
    TYPES = ['Point', 'Polygon', 'MultiPolygon']
    jsonObj = geojson.loads(obj)
    if len(jsonObj.keys()) == 2 and 'coordinates' in jsonObj.keys() and isinstance(jsonObj.get('coordinates'), list):
        if jsonObj.get('type') in TYPES:
            return jsonObj
        else:
            raise ValueError
    else:
        raise ValueError