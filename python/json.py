'''JSONdan ma'lumot olish, lekin mening kotpyuterim googlemaps nomli modulni yuklamayabdi'''



import json
import googlemaps
from apikey import APIKEY
#Google Maps
gmaps = googlemaps.Client(key=APIKEY)

geocode_result = gmaps.geocode('Sanchiqul, Samarkand, Uzbekistan')
#print(geocode_result)

g = json.dumps(geocode_result[0], indent = 4, sort_keys = True)
print(g)