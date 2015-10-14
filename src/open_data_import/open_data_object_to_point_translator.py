class OpenDataToPointTranslator(object):

    def __init__(
            self, importDataDict,
            objectRepresentation,
            version,
            importSource,
            channelId):
        self.objectRepresentation = objectRepresentation
        self.version = version
        self.importSource = importSource
        self.channelId = channelId
        self.importDataDict = importDataDict

    #@should_be_extended_in_descendents
    def getPointJson(self):
        obj = {}
        obj['version'] = self.version
        obj['import_source'] = self.importSource
        return obj

    #@should_be_extended_in_descendents
    def getPoint(self):
        point = {'json': self.getPointJson()}
        point['channel_id'] = self.channelId
        return point
