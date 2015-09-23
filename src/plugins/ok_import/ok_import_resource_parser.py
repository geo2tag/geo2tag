import sys
sys.path.append("../../open_data_import")
from od_import_parser import OdImportParser

CHANNEL_NAME = 'channelName'
OPEN_DATA_URL = 'openDataUrl'
SHOW_OBJECT_URL = 'showObjectUrl'
SHOW_IMAGE_URL = 'showImageUrl'


class OKImportParser(OdImportParser):

	mandatoryFields = [CHANNEL_NAME, OPEN_DATA_URL, SHOW_OBJECT_URL, SHOW_IMAGE_URL]
