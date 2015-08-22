from collections import defaultdict
d = defaultdict(list)
n,m = map(int, input().split())
for i in range (n):
    d['A'].append(input())
for i in range (m):
    d['B'].append(input())

res = {}
for j in range (m):
    res[d['B'][j]] = [(i+1) for i in range (n) if d['A'][i] == d['B'][j]]
    if not res[d['B'][j]]:
        print('-1')
        continue
    for k in range (len(res[d['B'][j]])):
        if k != len(res[d['B'][j]]) - 1: print(res[d['B'][j]][k], end=" ")
        else: print(res[d['B'][j]][k])
