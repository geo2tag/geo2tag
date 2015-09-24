import sys
import os
sys.path.append('../../open_data_import')
sys.path.append('../..')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'open_data_import/')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from open_data_to_points_loader import OpenDataToPointsLoader
import requests


class OpenKareliaObjectsLoader(OpenDataToPointsLoader):

    def __init__(self, loadUrl):
        self.loadUrl = loadUrl

    def load(self):
        return requests.get(self.loadUrl).text
