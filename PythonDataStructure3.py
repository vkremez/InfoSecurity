# University of Michigan

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
mydict = dict()
for line in handle:
	if line.startswith('From:'):
    	lst.append(line.split()[1])
for email in lst:
    if email not in mydict:
        mydict[email] = 1
    else:
        mydict[email] += 1
'''
another way to implement:
	for email in mydict:
   		mydict[email] = mydict.get(email,0) + 1
'''

bigcount = None
bignumber = None
for email,count in mydict.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count
        
print bigword, bigcount
