N = int(input())
c = []
m1 = m2 = 0
for i in range (N):
    c.append([input(), float(input())])
    if (i == 0): m1 = m2 = c[i][1]; continue
    if (m1 == m2 and c[i][1] != m1):
        if (c[i][1] < m1): m1 = c[i][1]; continue
        else: m2 = c[i][1]; continue
    if (c[i][1] < m1): m2 = m1; m1 = c[i][1]
    elif (c[i][1] < m2 and c[i][1] > m1): m2 = c[i][1]
ans = [c[i][0] for i in range (N) if (c[i][1] == m2)]
ans.sort()
for i in range (len(ans)):
    print (ans[i])
