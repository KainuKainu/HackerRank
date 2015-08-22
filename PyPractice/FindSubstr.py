S = input()
sub = input()
i = 0
count = 0
dif = len(S)
while i < dif:
    tmp = S.find(sub, i, dif)
    if tmp == -1: break
    else:
        i = tmp+1
        count +=1
print(count)
