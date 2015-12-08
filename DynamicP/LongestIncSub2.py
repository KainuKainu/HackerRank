from sys import stdin
N = int(input())
array = [int(num) for num in list(stdin.read().split())]
#print ("Original array: ", end="")
#print (array)

dp = [1]*N

for i in range (1,N):
    for j in range (i):
        if array[i] > array[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

#print (dp)
#print ("The answer is: ", end="")
print (max(dp))
