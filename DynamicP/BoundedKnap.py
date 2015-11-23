N,K = [int(num) for num in input().split()]
weight = [0] + [int(num) for num in input().split()]
value = [0] + [int(num) for num in input().split()]
dp = []
for _ in range (K+2):
    dp.append([0]*(N+1))

for w in range (1,K+1):
    for i in range (1,N+1):
        if (weight[i] <= w):
            tmp = dp[w-weight[i]][i-1] + value[i]
        else:
            tmp = 0
        dp[w][i] = max(tmp,dp[w][i-1])

print()
for w in range (0,K+1):
    for i in range (0,N+1):
        print(dp[w][i], end=" ")
    print()
print()
