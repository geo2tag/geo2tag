from flask_restful import reqparse

ARGS_LOG_SIZE = "logSize"

class PointParser():
    @staticmethod
    def parsePostParameters():
        args = validatePointsList(request.get_json(force=True))
        return args

def validatePointsList(json):
    if type(json) != type([]):
        raise ValueError
    for obj in json:
        if not ('lon' in obj.keys() and 'lat' in obj.keys() and 'alt' in obj.keys() and 'json' in obj.keys() and 'channel_id' in obj.keys()):
            raise ValueError
        else: 
            if not (type(obj['lat']) == int or type(obj['lat']) == float):
            	raise ValueError
            if not (type(obj['lon']) == int or type(obj['lon']) == float):
                raise ValueError
            if not (type(obj['alt']) == int or type(obj['alt']) == float):
                raise ValueError
            if not type(obj['json']) == dict:
            	raise ValueError
            if not type(obj['channel_id']) == str:
                raise ValueError
    return json