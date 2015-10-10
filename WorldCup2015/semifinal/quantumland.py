#Failteam
from sys import stdin
N = int(stdin.readline())
edges = [[0,0]]
next_start_nodes = set()
for i in range (1,N+1):
    edge = stdin.readline().split()
    edges.append([int(edge[0]), float(edge[1])])
    next_start_nodes.add(i)

ans = 0
#cycle_nodes = set()

while next_start_nodes:
    node = next_start_nodes.pop()
    prob = 1
    visited_nodes = set()
    visited_nodes.add(node)
    next_nodes = set()
    next_nodes.add(edges[node][0])
    curr_node = node
    while next_nodes:
        next_node = next_nodes.pop()
        #cycle finished
        if next_node == node:
            prob *= edges[curr_node][1]/100
            ans += prob
            #cycle_nodes.update(visited_nodes)
            next_start_nodes.difference_update(visited_nodes)
            continue
        #not cycle
        if next_node in visited_nodes:
            continue
        #still assuming cycle
        next_nodes.add(edges[next_node][0])
        visited_nodes.add(next_node)
        prob *= edges[curr_node][1]/100
        curr_node = next_node

#answer
print ("%.2f" % ans)
