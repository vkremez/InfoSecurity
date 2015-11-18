#University of Michigan Challenge For Python Programmers

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list() #declare a list
total = list() #--=--
for line in fh:
  lst.append(line.split()) #split all lines and append them to list 'lst'
for i in lst:
    total += i #concatenate lists with whitespaces and commas
total.sort() #sort the list alphabetically
mylist = list(set(total)) #remove duplicates from the list
print mylist
