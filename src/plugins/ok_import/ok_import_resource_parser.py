import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'open_data_import/')))
from od_import_parser import OdImportParser

CHANNEL_NAME = 'channelName'
OPEN_DATA_URL = 'openDataUrl'


class OKImportParser(OdImportParser):

	mandatoryFields = [CHANNEL_NAME, OPEN_DATA_URL, SHOW_OBJECT_URL, SHOW_IMAGE_URL]
