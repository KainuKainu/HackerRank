T = int(input())
while (T):
    T -= 1
    N,K = [int(num) for num in input().split()]
    maxAB = 0
    for a in range (1,N):
        for b in range (a+1,N+1):
            tmp = a & b
            if tmp == K-1:
                print (tmp)
                continue
            if tmp > maxAB and tmp < K:
                maxAB = tmp
    print (maxAB)
