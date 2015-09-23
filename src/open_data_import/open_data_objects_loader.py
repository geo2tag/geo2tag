class OpenDataObjectsLoader:

    def __init__(self, loadUrl):
        self.loadUrl = loadUrl

    def load(self):
        raise NotImplementedError()
