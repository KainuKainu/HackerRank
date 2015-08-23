# Python 3 solution for Maximize It
# Author: grabber
data = input().split()
k = int(data[0])
m = int(data[1])
states = [0]
for i in range(0, k):
    newstates = []
    data = input().split()
    #print(data[1:])
    for st in data[1:]:
        d = int(st)
        for s in states:
            newtot = (d*d + s) % m
            if not(newtot in newstates):
                newstates.append(newtot)
    states = newstates
#print (states)
print(max(states))
