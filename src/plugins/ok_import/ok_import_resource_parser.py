from od_import_parser import OdImportParser, CHANNEL_NAME, OPEN_DATA_URL 

SHOW_OBJECT_URL = 'showObjectUrl'
SHOW_IMAGE_URL = 'showImageUrl'

class OKImportParser(OdImportParser):

	mandatoryFields = [CHANNEL_NAME, OPEN_DATA_URL, SHOW_OBJECT_URL, SHOW_IMAGE_URL]
