#University of Michigan Challenge Python Data Structure

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()
mylist = list()
for line in fh:
    if line.startswith('From:'): #choose lines that begin with "From:"
        #print line.split()
        	print line.split()[1] #print the second element of the line
        	count += 1
print "There were", count, "lines in the file with From as the first word"
