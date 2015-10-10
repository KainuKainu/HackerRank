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
revisited = set()
while next_start_nodes:
    node = next_start_nodes.pop()
    visited_nodes = set()
    visited_nodes.add(node)
    next_nodes = set()
    next_nodes.add(edges[node][0])
    curr_node = node
    while next_nodes:
        next_node = next_nodes.pop()
        #no cycle
        if next_node in revisited:
            next_start_nodes.difference_update(visited_nodes)
            break
        #cycle found
        if next_node in visited_nodes:
            prob = 1
            loop_node = next_node
            prob *= edges[next_node][1]/100
            curr_node = edges[next_node][0]
            revisited.add(curr_node)
            while curr_node != loop_node:
                revisited.add(curr_node)
                prob *= edges[curr_node][1]/100
                curr_node = edges[curr_node][0]
            ans += prob
            next_start_nodes.difference_update(visited_nodes)
            break
        #still assuming cycle
        next_nodes.add(edges[next_node][0])
        visited_nodes.add(next_node)
        curr_node = next_node

#answer
print ("%.2f" % ans)
