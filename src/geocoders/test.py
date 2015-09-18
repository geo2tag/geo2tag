from geocoder_request import GeonamesRequestSender


test = ['Saint-Petersburg']
i = 0
while i<1000:

	GeonamesRequestSender.requestSingleCoordinates(str(i))
	i = i + 1
	print i