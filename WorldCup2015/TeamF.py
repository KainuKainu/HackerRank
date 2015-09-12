import sys
P = list(map(int,sys.stdin.read().split()))
P.sort(key=None,reverse=True)
ans = P[0] + P[2] + P[4]
print(ans)
