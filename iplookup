# _author_ = vkremez
#!/usr/bin/env python

from ipwhois import IPWhois
from pprint import pprint

def main():

f = open('ips.txt', 'r')
r = f.read()
s = n.split()
results = []
for i in s:
	obj = IPWhois(i)
	results.append(obj.get_countries())
	
#	bresults = results['nets']
#	cresults = results['query']
#	dresults = results['asn_registry']
#	eresults = results['as_country_code']
#	lst2.append(bresults)
w = open('results.txt', 'w')
w.write(str(results))
f.close()
w.close()

#if __name__ == "main":
#	print("iplookup is being run directly")
#else:	
#	print(iplookup is being imported into another module")
