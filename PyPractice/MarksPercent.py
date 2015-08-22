import sys
n = int(input())
D = {}
for i in range (0,n):
    l = input().split()
    name, marks = (l[0], l[1:])
    for u in range (0,len(marks)):
        marks[u] = float(marks[u])
    D[name] = marks

stu = input()
print ("%.2f" % (sum(D[stu])/len(D[stu])))
