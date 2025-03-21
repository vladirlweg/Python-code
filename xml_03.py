# The program will promp for a URL, read the XML data from that URL using urllib
# using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file and enter the sum.

# The program should do the followings:
# 1) Fetch the XML data from the URL
# 2) Parse the XML data
# 3) Extract the comments from the XML data
# 4) Sum up the comment counts and print it

import urllib.request
import xml.etree.ElementTree as ET

# sum of comments
sum_comments = 0

# prompt for the URL
url = input('Enter URL: ')

# fetch the XML data from the URL
data = urllib.request.urlopen(url)
xml_data = data.read()

# parse the XML data
tree = ET.ElementTree(ET.fromstring(xml_data))


for comment in tree.findall('.//comment'):
    # extract the count from each comment
    count = comment.find('count').text
    count = int(count)
    # sum up the comments
    sum_comments = sum_comments+count
    
print('The sum of the counts is:', sum_comments)