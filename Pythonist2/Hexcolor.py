import sys
N = input()
full = list(sys.stdin.read().split())
a = [full[i] for i in range (len(full)) if '#' in full[i] and (full[i+1]) !='{']
for i in range (len(a)):
    a[i] = (a[i])[a[i].find('#'):]
    for j in range (1,len(a[i])):
        t = ord((a[i])[j])
        if (t<ord('0')) or (t>ord('9') and t<ord('A')) \
                or (t>ord('Z') and t<ord('a')) or (t>ord('z')):
            a[i] = (a[i])[:j]
            break
for i in range (len(a)):
    if (len(a[i]) != 4 and len(a[i]) != 7):
        a[i] = 0
        continue
    for j in range (1,len(a[i])):
        t = ord((a[i])[j])
        if (t>ord('f') and t<ord('z')) or (t>ord('F') and t<ord('Z')):
            a[i] = 0
            break
for x in a:
    if x != 0: print(x)
