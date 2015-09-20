from datetime import datetime
import sys
sys.path.append('./src/open_data_import')
from open_data_object_to_point_translator import OpenDataToPointTranslator

class OpenKareliaObjectToPointTranslator(OpenDataToPointTranslator):

    def __init__(
            self,importDataDict,
            objectRepresentation,
            version,
            importSource,
            channelId):
        super().__init__(self,
            importDataDict,
            objectRepresentation,
            version,
            importSource,
            channelId)

    def getPointJson(self):
        obj = {}
        obj['name'] = self.objectRepresentation['name'][0]
        obj['image_url'] = self.importDataDict['image_url'] + \
            unicode(self.objectRepresentation.get('images', [{'$oid': ''}])[0]['$oid'])
        obj['source_url'] = self.importDataDict['source_url'] + \
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
        point['date'] = self.translateDate()
        point['bc'] = False
        return point

    def translateDate(self):
        try:
            if self.objectRepresentation.get('year') != None:
                return datetime(
                    int(self.objectRepresentation['year']), 1, 1, 0, 0)
            elif self.objectRepresentation.get('century') != None:
                return datetime(int(self.objectRepresentation[
                                'century']) * 100, 1, 1, 0, 0)
            elif self.objectRepresentation.get('millenium') != None:
                return datetime(int(self.objectRepresentation[
                                'millenium']) * 1000, 1, 1, 0, 0)
        finally:
            return datetime.now()
