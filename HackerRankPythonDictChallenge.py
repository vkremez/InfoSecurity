N = int(raw_input())
dc = dict()
lst1 = list()
for i in range(N):
    a = raw_input()
    lst1 = a.split()
    #print lst1
    d = lst1[0]
    #print d
    lst1.remove(lst1[0])
    #print lst1
    newlst1 = list(map(float, lst1))
    #print newlst1
    dc[d] = newlst1
name = raw_input()
#print dc
total = 0
if name in dc:
    marks = dc[name]
    no = len(marks)
    for num in marks:
        total += num
avg = total / no
print("%.2f" % avg)
