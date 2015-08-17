from datetime import datetime


class OpenKareliaObjectToPointTranslator:

    def __init__(self, serverShowImageUrl, serverShowObjectUrl,
                 objectRepresentation, version, importSource, channelId):
        self.serverShowImageUrl = serverShowImageUrl
        self.serverShowObjectUrl = serverShowObjectUrl
        self.objectRepresentation = objectRepresentation
        self.version = version
        self.importSource = importSource
        self.channelId = channelId

    def getPointJson(self):
        obj = {}
        obj['name'] = self.objectRepresentation['name'][0]
        obj['image_url'] = self.serverShowImageUrl
        obj['source_url'] = self.serverShowObjectUrl
        obj['version'] = self.version
        obj['import_source'] = self.importSource
        return obj

    def getPoint(self):
        point = {'json': self.getPointJson()}
        point['channelId'] = self.channelId
        point['location'] = {"type": "Point", "coordinates": [
            self.objectRepresentation['latitude'], self.objectRepresentation['longitude']]}
        point['alt'] = 0
        point['date'] = datetime.now()
        return point
