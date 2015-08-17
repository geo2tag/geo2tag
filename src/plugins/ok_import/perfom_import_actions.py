from datetime import datetime
from open_karelia_object_to_point_translator import getPoint

def performImportActions(odLoaderClass, odParserClass, \
    odToPointTranslatorClass, odToPointsLoaderClass, \
    serviceName, channelName, openDataUrl, \
    showObjectUrl, showImageUrl, serviceName):
     
    # uncomment in case of https://geo2tag.atlassian.net/browse/GT-1505
    '''if issubclassof(odLoaderClass, AbstractOpenDataLoader):
     
    if issubclassof(odParserClass, )
     
    if issubclassof(odToPointTranslatorClass, )
     
    if issubclassof(odToPointsLoaderClass, AbstractOpenDataToPointsLoader)
    '''
     
    channelId = getChannelIdByName(channelName)
    version = datetime.now()     
    loader = odLoaderClass(openDataUrl)
    openData = loader.load()
    parser = odParserClass(openData)
    objects = parser.parse()
    points = [ ]
     
    for object in objects:
        translator = odToPointTranslatorClass(showImageUrl, showObjectUrl, \
            object, version,openDataUrl, channelId)
        points.append(translator.getPoint())
     
    pointsLoader = odToPointsLoaderClass(serviceName, points)
    pointsLoader.loadPoints()
