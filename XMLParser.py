import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')
print 'Retrieving: ' + url
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print "Count: " + str(len(counts))
lst = tree.findall('comments/comment')
sum = 0
for item in lst:
    algorithm = int(item.find('count').text)
    sum =  algorithm + sum
print "Sum: " + str(sum)
