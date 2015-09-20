import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'open_data_import')))
from open_data_objects_parser import OpenDataObjectsParser


class OpenKareliaObjectsParser(OpenDataObjectsParser):

    def parse(self):
        obj = json.loads(self.data)
        return obj
