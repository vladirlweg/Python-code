# This program you will use a Geo Location lookup API to look up the location
# of some universities and parse the returned data.

# This program should do the followings:
# 1) Prompt for a location from the user
# 2) Use the OpenGeo API to retrieve the data for that location
# 3) Parse the return JSON to extract the plus_code
# 4) Handle the URL encoding of the query paramater (q)

import urllib.parse
import urllib.request
import json
import ssl
    
# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input user
address = input('Enter location: ')

# Use the OpenGeo API to retrieve the data for that location
address = address.strip()
parms = dict()
parms['q'] = address

# Create URL using uising input from user
url = serviceurl + urllib.parse.urlencode(parms)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

# Parse JSON data
js = json.loads(data)

print(js)