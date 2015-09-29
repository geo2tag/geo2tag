from abc import ABCMeta, abstractmethod


class OpenDataObjectsParser:
    __metaclass__ = ABCMeta

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def parse(self):
        pass
