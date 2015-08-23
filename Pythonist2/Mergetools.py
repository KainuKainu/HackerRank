S = input()
K = int(input())
N = len(S)
i = 0
p = []
while i < N:
    p.append(S[i:(i+K)])
    i += K

for tmp in p:
    d = {}
    for c in tmp: d[c] = 0
    for c in tmp: d[c] += 1
    for c in tmp:
        if d[c] > 0: print(c, end="")
        d[c] = 0
    print ("\n", end="")
