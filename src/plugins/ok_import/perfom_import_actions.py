from datetime import datetime
from db_model import getChannelByName

def performImportActions(odLoaderClass, odParserClass, \
    odToPointTranslatorClass, odToPointsLoaderClass, \
    channelName, openDataUrl, showObjectUrl, showImageUrl, serviceName):
     
    # uncomment in case of https://geo2tag.atlassian.net/browse/GT-1505
    '''if issubclassof(odLoaderClass, AbstractOpenDataLoader):
     
    if issubclassof(odParserClass, )
     
    if issubclassof(odToPointTranslatorClass, )
     
    if issubclassof(odToPointsLoaderClass, AbstractOpenDataToPointsLoader)
    '''
     
    channelId = getChannelByName(serviceName, channelName)['_id']
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
