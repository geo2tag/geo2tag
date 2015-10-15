from unittest import TestCase
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator

DATA1 = {
    'name': ['name'],
    'site': 'site',
    'latitude': float(100),
    'longitude': float(200)
}

DATA2 = {
    'name': ['name'],
    'site': 'site',
}


class TestSiteSaveImportFromOkPoint(TestCase):

    def testSiteSaveImportFromOkPoint1(self):
        okotpt = OpenKareliaObjectToPointTranslator(
            {'image_url': ''}, DATA1, None, None, None)
        p = okotpt.getPoint()
        self.assertEqual(p['json']['address'], 'site')
        self.assertEqual(p['location']['coordinates'][0], float(100))
        self.assertEqual(p['location']['coordinates'][1], float(200))

    def testSiteSaveImportFromOkPoint2(self):
        okotpt = OpenKareliaObjectToPointTranslator(
            {'image_url': ''}, DATA2, None, None, None)
        p = okotpt.getPoint()
        self.assertEqual(p['json']['address'], 'site')
        self.assertEqual(p['location']['coordinates'][0], float(0))
        self.assertEqual(p['location']['coordinates'][1], float(0))
