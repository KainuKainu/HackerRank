Q = int(input())
dp = {}
S = "01"
a = 1
b = 1
c = True
dp[1] = 1
while (Q):
    Q -= 1
    K,N = [int(num) for num in input().split()]
    if N in dp:
        print (dp[N]) if K == 1 else print (N-dp[N])
        #print(dp[N], N-dp[N])
    else:
        while a <= N:
            if S[b] == '1':
                if c:
                    S += "2" if S[a] == '1' else "1"
                    dp[a+1] = (dp[a]+1) if S[a] == '2' else (dp[a])
                    a += 1
                else:
                    if S[a] == '1':
                        S += "21"
                        dp[a+1] = dp[a]
                        dp[a+2] = dp[a]+1
                    else:
                        S += "12"
                        dp[a+1] = dp[a+2] = dp[a]+1
                    c = True
                    a += 2
            else:
                if c:
                    S += S[a]
                    dp[a+1] = (dp[a]+1) if S[a] == '1' else (dp[a])
                    c = False
                    a += 1
                else:
                    if S[a] == '1':
                        S += "22"
                        dp[a+1] = dp[a+2] = dp[a]
                    else:
                        dp[a+1] = dp[a]+1
                        dp[a+2] = dp[a]+2
                        S += "11"
                    a += 2
            b += 1
        print (dp[N]) if K == 1 else print (N-dp[N])
        #print(dp[N], N-dp[N])
    #print(S)
#print("Final dp")
#for i in dp:
    #print(dp[i])
