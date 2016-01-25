# MIT by Vitali
#! /usr/bin/env python
s = raw_input()

vow = []
for i in s:
     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
         vow.append(i)
print "Number of vowels:",  len(vow)
