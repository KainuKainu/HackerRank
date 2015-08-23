S = input()
L = len(S)
p1 = p2 = 0
for i in range (L):
    if S[i] in ['A', 'E', 'I', 'O', 'U']: p2 += L-i
    else: p1 += L-i
if p1 == p2: print ("Draw")
else: print ("%s %d" % (('Kevin', p2) if p2>p1 else ('Stuart', p1)))
