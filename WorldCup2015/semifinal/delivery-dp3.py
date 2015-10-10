# True if there's path from a to b, else False
def has_path(a,b):
    global dp,edges
    #same node
    if a == b:
        return True
    #already in dp
    if dp.has_key((a,b)):
        return dp[(a,b)]
    #loop thru edges
    next_nodes = edges[a][:]
    while next_nodes:
        next_node = next_nodes.pop()
        dp[(a,next_node)] = True
        if has_path(next_node,b) == True:
            dp[(a,b)] = True
            return True
    dp[(a,b)] = False
    return False


import sys
T = int(sys.stdin.readline())
sys.setrecursionlimit(100000)
for _ in range (T):
    #input
    dp = {}
    N,M,K = [int(num) for num in sys.stdin.readline().split()]
    K_nodes = [int(num) for num in sys.stdin.readline().split()]
    if K == 1:
        print K_nodes[0]
        continue
    K_nodes.sort(None,None,True)
    edges = []
    for _ in range (N+1):
        edges.append([])
    for _ in range (M):
        x,y = [int(num) for num in sys.stdin.readline().split()]
        edges[x].append(y)
    for i in range (N+1):
        edges[i].sort()

    #testing has_path()
    '''
    print "case (1,4):", has_path(1,4)
    print "case (3,4):", has_path(3,4)
    print "case (3,2):", has_path(3,2)
    print "case (4,2):", has_path(4,2)
    print "case (2,3):", has_path(2,3)
    exit()
    '''

    #start from each node in list K
    start_nodes = K_nodes[:]
    while start_nodes:
        possible = True
        node = start_nodes.pop()
        path = [node]
        next_nodes = K_nodes[:]
        next_nodes.remove(node)
        curr_node = node
        while next_nodes:
            next_node = next_nodes.pop()
            #print "curr_node =", curr_node
            #print "next_node =", next_node
            #print has_path(curr_node, next_node)
            if has_path(curr_node, next_node) == False:
                possible = False
                break
            path.append(next_node)
            curr_node = next_node
        if possible:
            break

    #path found
    #print (path if possible else "-1")
    if possible:
        for node in path:
            print node,
    else:
        print "-1",
    print ""
