N = int(input())
l = list(map(int, input().split()))
n1 = n2 = -100
for i in range (N):
    if (l[i] > n1): n2 = n1; n1 = l[i]
    elif (l[i] > n2 and l[i] < n1): n2 = l[i]
print (n2)
