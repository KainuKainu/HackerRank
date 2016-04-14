T = int(input())
D = 1
while D <= T:
    print("Case #" + str(D) + ":",end="")
    K,C,S = [int(num) for num in input().split()]
    #impossible
    if C*S<K:
        print(" IMPOSSIBLE")
    #possible
    else:
        for lasti in range(1,K+1,C):
            index = 1
            for i in range(lasti,lasti+C):
                if i>K:
                    index = (index-1)*K + K
                    break
                else:
                    index = (index-1)*K + i
            print(" " + str(index),end="")
        print("")
    D += 1
