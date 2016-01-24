from pygeocoder import Geocoder

def getCoordinates(address):
	results = Geocoder.geocode(str(address))
	return results[0].coordinates