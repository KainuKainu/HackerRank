from sys import stdin
N = int(input())
array = [0] + [int(num) for num in list(stdin.read().split())]
#print ("Original array: ", end="")
#print (array)

dp = []
for _ in range (N+1):
    dp.append([1]*(N+1))

for i in range (1,N+1):
    for j in range (1,N+1):
        if (array[j] > array[i] and array[j] > array[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

for i in range (N+1):
    for j in range (N+1):
        print (dp[i][j], end=" ")
    print ()

print ("The answer is: ", end="")
print (dp[N][N]+1)
