# The program will use urllib to read the HTML from the data files below, extract
# the href=values from the anchor tages, can for a tag that is in a particular 
# position from the top and follow that link, repeat the process a number of times,
# and report the last name you find.

# The program should do the followings:
# 1) Read an HTML page.
# 2) Extract all href values from <a> tags
# 3) Follow the link at a specific position.
# 4) Repeat the process for a given number of iterations.
# 5) Print the last name found in the final URL.

import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Function to extract the link at a specific position
def get_link_at_specific_position(position, url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    # Read HTML content
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all tags
    tags = soup.find_all('a')
    
    # Check if the desired position is within the range
    if len(tags) >= position:
        return tags[position-1].get('href')
    else:
        return None
    
#input from user
url = input('Enter the starting URL: ').strip()
position = int(input('Enter the position of the link: '))
count = int(input('Enter the number of times to repeat: '))

current_url = url
for counter in range(count):
    next_url = get_link_at_specific_position(position, current_url)
    if next_url is None:
        break
    current_url = next_url
    print(current_url)

print('Last url reached is:', current_url)    