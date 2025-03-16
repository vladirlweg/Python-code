# Download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
import ssl
import re
from bs4 import BeautifulSoup

total = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
#html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
   # print(tag.get('href',None))
    

text = soup.get_text()    

numbers = re.findall(r'\d+\.?\d*', text)

print(numbers)


for num in numbers:
    total = total+float(num)

print(total)