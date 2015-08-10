import requests
class OpenKareliaObjectsLoader:
    def __init__(self, loadUrl):
        self.loadUrl = loadUrl

    def load(self):
    	print self.loadUrl, '1111111111111111111111111111111111111111'
        return requests.get(self.loadUrl).text
