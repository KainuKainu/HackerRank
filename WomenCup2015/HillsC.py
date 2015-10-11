import sys
sys.setrecursionlimit(100000)
def has_path(a,b):
    #same node
    if a == b:
        dp[(a,b)] = True
    #already in dp
    if (a,b) not in dp:
        #loop thru edges
        dp[(a,b)] = False
        next_nodes = edges[a][:]
        for next_node in next_nodes:
            dp[(a, next_node)] = True
            partial = has_path(next_node, b)
            if partial:
                dp[(a, b)] = True
                break
    return dp[(a,b)]

T = int(input())
while (T):
    T -= 1
    N,M = [int(num) for num in input().split()]
    dp = {}
    fail = False
    nodes = [0]*(N+1)
    found = [0]*(N+1)
    edges = []
    for i in range (N+2):
        edges.append([])
    while (M):
        M -= 1
        a,b = [int(num) for num in input().split()]
        nodes[a] -= 1
        nodes[b] += 1
        edges[a].append(b)
        found[a] = found[b] = 1
    if found[1] == 0 or found[N] == 0:
        print("Danger!! Lucifer will trap you")
        continue
    for i in range (1,N+1):
        if nodes[i] != 0 and found[i] == 1:
            print("Danger!! Lucifer will trap you")
            fail = True
            break
    if not fail:
        for i in range (2,N+1):
            if found[i] == 0:
                continue
            if has_path(1,i) == False:
                print("Danger!! Lucifer will trap you")
                fail = True
                break
        if not fail:
            print("Go on get the Magical Lamp")
