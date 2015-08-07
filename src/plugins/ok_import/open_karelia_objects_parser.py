import json

class OpenKareliaObjectsParser:
    def __init__(self, data):
        self.data = data

    def parse(self):
        obj = json.loads(self.data)
        return obj