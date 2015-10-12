import json
import os
from open_data_objects_parser import OpenDataObjectsParser


class OpenKareliaObjectsParser(OpenDataObjectsParser):

    def parse(self):
        obj = json.loads(self.data)
        return obj
