# University of Michigan

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
lst2 = list()
mydict = dict()
for line in handle:
    if line.startswith('From '):
		lst.append(line.split()[5])
for string in lst:
    lst2.append(string.split(':')[0])
        
for email in lst2:
    if email not in mydict:
        mydict[email] = 1
    else:
        mydict[email] += 1

for k, v in sorted(mydict.items()):
    print k, v
