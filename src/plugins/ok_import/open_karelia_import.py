from perfom_import_actions import performImportActions
from open_karelia_objects_loader import OpenKareliaObjectsLoader
from open_karelia_objects_parser import OpenKareliaObjectsParser
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator
from open_karelia_data_to_points_loader import OpenKareliaDataToPointsLoader


def openKareliaImport(
        self,
        channelName,
        openDataUrl,
        showObjectUrl,
        showImageUrl,
        serviceName):
    performImportActions(
        OpenKareliaObjectsLoader,
        OpenKareliaObjectsParser,
        OpenKareliaObjectToPointTranslator,
        OpenKareliaDataToPointsLoader,
        channelName,
        openDataUrl,
        showObjectUrl,
        showImageUrl,
        serviceName)
    self.callBack()
