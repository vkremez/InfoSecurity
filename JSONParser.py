#__author__ = 'vkremez'
import urllib
import json

selecturl = raw_input("Enter location: ")
u = urllib.urlopen(selecturl)
print "Retrieving ", selecturl
data = u.read()
info = json.loads(data)
print data
print "Retrieved ",len(data)," characters"
sum = 0
print "Count: ", len(info['comments'])
for x in info['comments']:
    y= (x['count'])
    sum = y + sum
print sum
