#!/bin/usr/env python
# MIT by Vitali 
# Prints count of substring occurrences in a string

s = raw_input()
start=0
count=0 
while start<=len(s):
    n=s.find('b',start,len(s))
    prnt=(s[start:start+3])
    if prnt =='bob':
       start=n+2 
       count+=1
    else:
        start+=1        
print "Number of times bob occurs is:",  count
