from abc import ABCMeta, abstractmethod


class OpenDataObjectsLoader:
    __metaclass__ = ABCMeta

    def __init__(self, loadUrl):
        self.loadUrl = loadUrl

    @abstractmethod
    def load(self):
        raise NotImplementedError()
