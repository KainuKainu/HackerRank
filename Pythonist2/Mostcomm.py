S = input()
d = {}
m = [0]*3
val = [None]*3
for i in range (ord('a'),ord('z')+1):
    d[i] = 0
for c in S:
    d[ord(c)] += 1

for i in range (ord('a'),ord('z')+1):
    if d[i] > m[0]:
        m[2], val[2] = (m[1], val[1])
        m[1], val[1] = (m[0], val[0])
        m[0], val[0] = (d[i], i)
        continue
    if d[i] > m[1]:
        m[2], val[2] = (m[1], val[1])
        m[1], val[1] = (d[i], i)
        continue
    if d[i] > m[2]:
        m[2], val[2] = (d[i], i)
        continue

for i in range (3):
    print ("%c %d" % (val[i], m[i]))
