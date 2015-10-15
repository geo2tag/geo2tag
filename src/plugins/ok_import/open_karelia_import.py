from perform_import_actions import performImportActions
from open_karelia_objects_loader import OpenKareliaObjectsLoader
from open_karelia_objects_parser import OpenKareliaObjectsParser
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator
from open_data_to_points_loader import OpenDataToPointsLoader


def openKareliaImport(
        self,
        channelName,
        openDataUrl,
        showObjectUrl,
        showImageUrl,
        serviceName):
    importDataDict = {
        'showImageUrl': showImageUrl,
        'showObjectUrl': showObjectUrl}
    performImportActions(
        OpenKareliaObjectsLoader,
        OpenKareliaObjectsParser,
        OpenKareliaObjectToPointTranslator,
        OpenDataToPointsLoader,
        channelName,
        openDataUrl,
        importDataDict,
        serviceName)
    return None
