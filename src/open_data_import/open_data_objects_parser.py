import json
import abc


class OpenDataObjectsParser:

    def __init__(self, data):
        self.data = data

    @abc.abstractmethod
    def parse(self):
        pass
