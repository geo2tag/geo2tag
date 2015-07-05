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
		print obj.keys()
		if not ('lon' in obj.keys() and 'lat' in obj.keys() and 'alt' in obj.keys() and 'json' in obj.keys() and 'channel_id' in obj.keys()):
			raise ValueError
		else: 
			if not ((type(obj['lat']) == type(1) or type(obj['lat']) == type(1.1)) and (type(obj['lon']) == type(1) or type(obj['lon']) == type(1.1))):
				raise ValueError
			if not (type(obj['alt']) == type(1) or type(obj['alt']) == type(1.1)):
				raise ValueError
			if not (type(obj['json']) == type({}) and type(obj['channel_id']) == type('')):
				raise ValueError
	return json