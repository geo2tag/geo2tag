import requests
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'open_data_import/'))
from open_data_objects_loader import OpenDataObjectsLoader


class OpenKareliaObjectsLoader(OpenDataObjectsLoader):

    def load(self):
        return requests.get(self.loadUrl).text
