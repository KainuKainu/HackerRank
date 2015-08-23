S = input()
ans = ''
for i in range (len(S)):
    ans += S[i].upper() if S[i].islower() else S[i].lower()
print(ans)
