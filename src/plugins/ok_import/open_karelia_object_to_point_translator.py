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
            unicode(self.objectRepresentation.get('images', [u''])[0])
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
        point['date'] = self.translateDate()
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
