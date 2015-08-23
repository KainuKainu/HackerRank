S = input()
L = len(S)
words = [S[i:j+1] for i in range(L) for j in range(i,L)]
p1 = p2 = 0
for x in words:
    if x[0] in ['A', 'E', 'I', 'O', 'U']: p2 +=1
    else: p1 +=1
if p1 == p2: print ("Draw")
else: print ("%s %d" % (('Kevin', p2) if p2>p1 else ('Stuart', p1)))
