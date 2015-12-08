n,m = [int(num) for num in input().split()]
A = [0] + [int(num) for num in input().split()]
B = [0] + [int(num) for num in input().split()]

dp = []
for _ in range (n+1):
    dp.append([0]*(m+1))

for i in range (1,n+1):
    for j in range (1,m+1):
        if (A[i] == B[j]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print (dp[n][m])
