def score(S, sub):
    i = count = 0
    dif = len(S)
    while i < dif:
        tmp = S.find(sub, i, dif)
        if tmp == -1: break
        else:
            i = tmp+1
            count +=1
    return count

S = input()
L = len(S)
vow = ['A', 'E', 'I', 'O', 'U']
d = {'Stuart': 0, 'Kevin': 0}
a = {}
alrdy = []
for i in range (L):
    for j in range (i+1, L+1):
        tmp = S[i:j]
        if tmp not in alrdy:
            scr = score(S, S[i:j])
            if tmp[0] in vow: d['Kevin'] += scr
            else: d['Stuart'] += scr
            alrdy.append(S[i:j])

if d['Kevin'] == d['Stuart']: print('Draw')
else: print ("%s %d" % (('Kevin',d['Kevin']) if d['Kevin']>d['Stuart'] \
        else ('Stuart',d['Stuart'])))
