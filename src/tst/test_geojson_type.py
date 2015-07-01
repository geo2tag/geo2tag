import geojson
from unittest import TestCase
import sys
sys.path.append('../')
import geo_json_type
TEST_POINT = '{"coordinates": [-115.8, 37.2], "type": "Point"}'
BAD_TEST_POINT = ['{"coordinate": [-115.8, 37.2], "type": "Point"}', 
'{"coordinate": [-115.8, 37.2], "type": "Point"}', 
'{"coordinates": [-115,8, 37.2], "type": "Pont"}',
'{"coordinates": -115.8, 37.2], "type": "Point"}']

TEST_POLYGON = '{"coordinates": [[[2.3, 57.32], [23.19, -20.2], [-120.4, 19.1]]], "type": "Polygon"}'
BAD_TEST_POLYGON = ['{"coordintes": [[[2.3, 57.32], [23.19, -20.2], [-120.4, 19.1]]], "type": "Polygon"}',
'{"coordinates": [[2.3, 57.32], [23.19, -20.2], [-120.4, 19.1]]], "type": "Polygon"}',
'{"coordinates": [[[2.3, 57.32], [23.19 -20.2], [-120.4, 19.1]]], "type": "Polygon"}',
'{"coordinates": [[[2.3, 57.32] [23.19, -20.2], [-120.4, 19.1]]], "type": "Polygon"}',
'{"coordinates": [[[2.3, 57.32], [23.19, -20.2], [-120.4, 19.1]]], "type": "Poligon"}',
'{"coordinates": [[[2.3, 57.32], [23.19, -20.2], [-120.4, 19.1]]], "tipe": "Polygon"}']
TEST_MULTI_POLYGON = '{"coordinates": [[[[3.7, 9.2], [-130.9, 1.5], [35.1, 72.23]]], [[[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]]], "type": "MultiPolygon"}'
BAD_TEST_MULTI_POLYGON = [ '{"coordinates": [[[[3.7, 9.2], [-130.9, 1.5], [35.1, 72.23]]], [[[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]]], "type": "MultiPolygo"}',
'{"coordiates": [[[[3.7, 9.2], [-130.9, 1.5], [35.1, 72.23]]], [[[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]]], "type": "MultiPolygon"}',
'{"coordinates": [[[3.7, 9.2], [-130.9, 1.5], [35.1, 72.23]]], [[[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]]], "type": "MultiPolygon"}',
'{"coordinates": [[[[3.7, 9.2], [-130.9 1.5], [35.1, 72.23]]], [[[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]]], "type": "MultiPolygon"}',
'{"coordinates": [[[[3.7, 9.2], [-130.9, 1.5] [35.1, 72.23]]], [[[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]]], "type": "MultiPolygon"}',
'{"coordinates": [[[[3.7, 9.2], [-130.9, 1.5], [35.1, 72.23]]], [[[23.1, -34.2], [-1.3, -4.6], [3.4, 77.9]]]], "typ": "MultiPolygon"}']
class TestGeoJson(TestCase):
    def testGeoJson(self):
        obj = geo_json_type.GeoJsonType(TEST_POINT)
        print obj
        for point in BAD_TEST_POINT:
            with self.assertRaises(ValueError):
                obj = geo_json_type.GeoJsonType(point)
        obj = geo_json_type.GeoJsonType(TEST_POLYGON)
        print obj
        for polygon in BAD_TEST_POLYGON:
            with self.assertRaises(ValueError):
                obj = geo_json_type.GeoJsonType(polygon)
        obj = geo_json_type.GeoJsonType(TEST_MULTI_POLYGON)
        print obj
        for multi_polygon in BAD_TEST_POLYGON:
            with self.assertRaises(ValueError):
                obj = geo_json_type.GeoJsonType(multi_polygon)