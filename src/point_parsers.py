from flask_restful import reqparse

ARGS_LOG_SIZE = "logSize"

class PointParser():
    @staticmethod
    def parsePostParameters():
        args = validatePointsList(request.get_json(force=True))
        return args

def validatePointsList(json):
    if type(json) != list:
        raise ValueError('Value is not a list')
    for obj in json:
        if not ('lon' in obj.keys() and 'lat' in obj.keys() and 'alt' in obj.keys() and 'json' in obj.keys() and 'channel_id' in obj.keys()):
            raise ValueError('Incorrect keys')
        else: 
            if not (type(obj['lat']) == int or type(obj['lat']) == float):
            	raise ValueError("'lat' - Incorrect type")
            if not (type(obj['lon']) == int or type(obj['lon']) == float):
                raise ValueError("'lon' - Incorrect type")
            if not (type(obj['alt']) == int or type(obj['alt']) == float):
                raise ValueError("'alt' - Incorrect type")
            if not type(obj['json']) == dict:
            	raise ValueError("'json' - Incorrect type")
            if not type(obj['channel_id']) == str:
                raise ValueError("'channel_id' - Incorrect type")
    return json