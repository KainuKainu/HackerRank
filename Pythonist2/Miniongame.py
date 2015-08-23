def score(S, sub, L):
    i = count = 0
    while i < L:
        tmp = S.find(sub, i, L)
        if tmp == -1: break
        else:
            i = tmp+1
            count +=1
    return count

S = input()
L = len(S)
vow = ['A', 'E', 'I', 'O', 'U']
d = [0]*2
full = {S[i:j+1] for i in range(L) for j in range(i,L)}
for sub in full:
    if sub[0] in vow: d[0] += score(S,sub,L)
    else: d[1] += score(S,sub,L)

if d[0] == d[1]: print('Draw')
else: print ("%s %d" % (('Kevin',d[0]) if d[0]>d[1] else ('Stuart',d[1])))
