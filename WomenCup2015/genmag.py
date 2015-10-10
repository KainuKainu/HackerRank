S = "01"
a = 1
b = 1
c = True
while a < 18:
    if S[b] == '1':
        if c:
            S += "2" if S[a] == '1' else "1"
            a += 1
        else:
            S += "21" if S[a] == '1' else "12"
            c = True
            a += 2
    else:
        if c:
            S += S[a]
            c = False
            a += 1
        else:
            S += "22" if S[a] == '1' else "11"
            a += 2
    b += 1
print (S)
