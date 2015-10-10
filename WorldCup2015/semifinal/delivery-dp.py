# True if there's path from a to b, else False
def has_path(a,b):
    global dp,edges
    #already in dp
    if dp.has_key((a,b)):
        return dp[(a,b)]
    #loop thru edges
    next_edges = filter(lambda edge: edge[0] == a, edges)
    while next_edges:
        next_node = next_edges.pop()[1]
        if next_node == b:
            dp[(a,b)] = True
            return True
        tmp = filter(lambda edge: edge[0] == next_node, edges)
        next_edges += tmp
    dp[(a,b)] = False
    return False


from sys import stdin
T = int(stdin.readline())
for _ in range (T):
    #input
    dp = {}
    N,M,K = [int(num) for num in stdin.readline().split()]
    K_nodes = [int(num) for num in stdin.readline().split()]
    if K == 1:
        print K_nodes[0]
        continue
    K_nodes.sort(None,None,True)
    edges = []
    for _ in range (M):
        edges.append([int(num) for num in stdin.readline().split()])
    edges.sort()

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
        print "-1"
    print ""
