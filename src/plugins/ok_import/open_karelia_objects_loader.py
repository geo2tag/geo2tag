import requests
from open_data_objects_loader import OpenDataObjectsLoader


class OpenKareliaObjectsLoader(OpenDataObjectsLoader):

    def load(self):
        return requests.get(self.loadUrl).text
