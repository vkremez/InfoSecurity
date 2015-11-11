#_author = vkremez

# This is an assignment for University of Michigan's course on # "Using Python to Access Web Data."


# Basically, this Python script will allow us to scrape # the content of a website for any URLs. 

# Here is the algorithm:
'''
The program will use urllib to (1) read the HTML from the website data, (2) extract the href= values from the anchor tags, (3) scan for a tag that is in a particular position relative to the first name in the list, (4) follow that link and repeat the process a number of times and report the results.
'''
import urllib
from bs4 import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup('a')

count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

print "Retrieving: " + url
print "Retrieving: " + tags[position-1].get('href', None)

for x in range(0,count-1):
  html = urllib.urlopen(tags[position-1].get('href',None)).read()
  soup = BeautifulSoup(html) tags = soup('a')
  print "Retrieving: " + tags[position-1].get('href', None)
