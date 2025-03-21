# The program will prompt for a URL, read the JSON data from that URL using
# urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file

# The program should do the followings:
# 1) Fetch the JSON data from the URL
# 2) Parse the JSON data
# 3) Extract the comments from the JSON data
# 4) Sum up all the comments

import json, urllib.request

# sum of comments
sum_comments = 0

# prompt for the url
url = input('Enter url: ')

# fetch the JSON data from the URL
data = urllib.request.urlopen(url)
JSON_data = data.read()

# parse JSON data
tree = json.loads(JSON_data)

for comment in tree.get('comments'):
    # extract the count from each comment
    count = comment.get('count')
    count = int(count)
    # sum up the comments
    sum_comments = sum_comments+count
    
print('The sum of the counts is:', sum_comments)