T = int(input())
while (T):
    T -= 1
    N,K = [int(num) for num in input().split()]
    for p in range (K-1,-1,-1):
        tmp = '0' + str(bin(p))[2:]
        #print ("p = %d, tmp = %s" % (p,tmp))
        x = len(tmp)-1
        while tmp[x] != '0' and x >= 0:
            x -= 1
        if x == -1:
            continue
        #print ("x = %d" % (x))
        B = tmp[:x] + '1' + tmp[(x+1):]
        b = int(B,2)
        if b <= N:
            break
    print (p)
