# True if there's path from a to b, else False
dp = {}
edges = {}
visit_all = [], -1
def has_path(a,b):
    #same node
    if a == b:
        dp[(a,b)] = True
    #already in dp
    if not dp.has_key((a,b)):
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

def can_visit_all(current, nodes):
    if not nodes:
        return [current], 0
    result = [], -1
    for next_node in nodes:
        if has_path(current, next_node):
            new_next_node = nodes[:]
            new_next_node.remove(next_node)
            next_path = can_visit_all(next_node, new_next_node)
            if next_path[1] != -1:
                result = ([current] + next_path[0]), 0
        if result[1] == 0:
            break
    return result

import sys
T = int(sys.stdin.readline())
sys.setrecursionlimit(100000)
for _ in range(T):
    #input
    dp = {}
    visit_all = [], -1
    N,M,K = [int(num) for num in sys.stdin.readline().split()]
    K_nodes = [int(num) for num in sys.stdin.readline().split()]
    if K == 1:
        print K_nodes[0]
        continue
    K_nodes.sort()
    edges = {}
    for i in range (N+1):
        edges[i] = []
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
    for node in start_nodes:
        next_nodes = start_nodes[:]
        next_nodes.remove(node)
        visit_all = can_visit_all(node, next_nodes)
        if visit_all[1] == 0:
            break

    #path found
    #print (path if possible else "-1")
    if visit_all[1] == 0:
        for node in visit_all[0]:
            print node,
    else:
        print "-1",
    print ""
