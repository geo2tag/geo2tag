from open_karelia_objects_loader import OpenKareliaObjectsLoader
from open_karelia_objects_parser import OpenKareliaObjectsParser
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator
from open_karelia_data_to_points_loader import OpenKareliaDataToPointsLoader
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../', 'open_data_import/')))
from perform_import_actions import performImportActions


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
    self.stop()
