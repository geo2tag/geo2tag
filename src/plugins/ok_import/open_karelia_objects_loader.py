import sys
import os
sys.path.append('../../open_data_import')
sys.path.append('../..')
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            '..',
            'open_data_import/')))
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            '..')))
from open_data_to_points_loader import OpenDataToPointsLoader
import requests
import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'open_data_import/'))
from open_data_objects_loader import OpenDataObjectsLoader


class OpenKareliaObjectsLoader(OpenDataObjectsLoader):

    def load(self):
        return requests.get(self.loadUrl).text
