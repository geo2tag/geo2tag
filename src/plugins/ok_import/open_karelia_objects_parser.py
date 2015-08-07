import json

class OpenKareliaObjectsParser:
    def __init__(self, data):
        self.data = data

    def parse(self):
        obj = json.loads(self.data)
        return obj

o = OpenKareliaObjectsParser('[{"name": "test1"}, {"name": "test2"}]')
obj = o.parse()
print obj[0]