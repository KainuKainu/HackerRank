T = int(input())
while T>0:
    N,K = [int(num) for num in input().split()]
    items = [0] + [int(num) for num in input().split()]
    dp = [0]*(K+1)

    for w in range (1,K+1):
        tmp = 0
        for i in range (1,N+1):
            item = items[i]
            if (item <= w):
                tmp = dp[w - item] + item
                if (tmp > dp[w]):
                    dp[w] = tmp

    print(dp[K])
    T -= 1
