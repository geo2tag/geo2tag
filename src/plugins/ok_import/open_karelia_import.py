import sys
sys.path.append('/var/www/geomongo/open_data_import')
from perform_import_actions import performImportActions
from open_karelia_objects_loader import OpenKareliaObjectsLoader
from open_karelia_objects_parser import OpenKareliaObjectsParser
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator


def openKareliaImport(
        self,
        channelName,
        openDataUrl,
        showObjectUrl,
        showImageUrl,
        serviceName):
    importDataDict = {'showImageUrl': showImageUrl, 'showObjectUrl': showObjectUrl}
    performImportActions(
        OpenKareliaObjectsLoader,
        OpenKareliaObjectsParser,
        OpenKareliaObjectToPointTranslator,
        channelName,
        openDataUrl,
        importDataDict,
        serviceName)
    self.stop()
