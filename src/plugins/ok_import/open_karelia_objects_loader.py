import requests


class OpenKareliaObjectsLoader:

    def __init__(self, loadUrl):
        self.loadUrl = loadUrl

    def load(self):
        return requests.get(self.loadUrl).text
