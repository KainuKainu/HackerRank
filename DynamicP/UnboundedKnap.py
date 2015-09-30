T = int(input())
while T>0:
    N,K = [int(num) for num in input().split()]
    items = [0] + [int(num) for num in input().split()]
    dp = []
    for _ in range (K+2):
        dp.append([0]*(N+1))

    for s in range (1,K+1):
        for i in range (1,N+1):
            if s % items[i] == 0:
                dp[s][i] = s
            else:
                tmp = s - items[i]
                tmp = dp[tmp][i] if tmp >= 0 else dp[s-1][i]
                x = tmp + items[i] if tmp + items[i] <= s else tmp
                y = dp[s][i-1] + items[i] if (dp[s][i-1] + items[i] <= s) else dp[s][i-1]
                (dp[s])[i] = max(x,y)

    print (dp[K][N])
    T -= 1
