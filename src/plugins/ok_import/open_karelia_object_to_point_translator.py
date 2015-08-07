# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

class OpenKareliaObjectToPointTranslator:
    def __init__(self, serverShowImageUrl, serverShowObjectUrl, objectRepresentation, version, importSource, channelId):
        self.serverShowImageUrl = serverShowImageUrl
        self.serverShowObjectUrl = serverShowObjectUrl
        self.objectRepresentation = objectRepresentation
        self.version = version
        self.importSource = importSource
        self.channelId = channelId

    def getPointJson(self):
        obj = {}
        obj['name'] = self.objectRepresentation['name']
        obj['image_url'] = self.serverShowImageUrl
        obj['source_url'] = self.serverShowObjectUrl
        obj['version'] = self.version
        obj['import_source'] = self.importSource
        return obj

    def getPoint(self):
        point = {}
        point = self.getPointJson()
        point['channelId'] = self.channelId
        return point

o = OpenKareliaObjectToPointTranslator('image_url', 'object_url', {'name':'test'}, 'test_version', 'test_import', ['channelId1', 'channelId2'])
obj = o.getPoint()
print obj

#if __name__ == '__main__':
    #app.run()