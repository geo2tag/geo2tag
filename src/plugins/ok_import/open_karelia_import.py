from perfom_import_actions import performImportActions
from open_karelia_objects_loader import OpenKareliaObjectsLoader
from open_karelia_objects_parser import OpenKareliaObjectsParser
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator

def openKareliaImport(self, callback, channelName, openDataUrl, showObjectUrl, showImageUrl, serviceName):
    performImportActions(self, callback, OpenKareliaObjectsLoader, OpenKareliaObjectsParser, \
        OpenKareliaObjectToPointTranslator, OpenDataToPointsLoader, channelName, \
        openDataUrl, showObjectUrl, showImageUrl, serviceName)

