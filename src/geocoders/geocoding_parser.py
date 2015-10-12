import sys
sys.path.append('/var/www/geomongo/open_data_import/')
from od_import_parser import OdImportParser

CHANNEL_NAME = 'channelName'


class GeocodingParser(OdImportParser):

    mandatoryFields = [CHANNEL_NAME]
