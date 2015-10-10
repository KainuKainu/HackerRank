def distance(a,b):
    global dp,edges,N
    if a == b:
        return 0
    if dp[a][b] != -1:
        return dp[a][b]
    #dijkstra
    shortest = [0] + [sys.maxint]*N
    shortest[a] = 0
    visited = set()
    queue = [[a,0]]
    while queue:
        curr = queue.pop()
        if curr[0] in visited:
            continue
        visited.add(curr[0])
        for e in edges[curr[0]]:
            if e[0] in visited:
                continue
            tmp = curr[1] + e[1]
            if tmp < shortest[e[0]]:
                shortest[e[0]] = tmp
                dp[a][e[0]] = dp[e[0]][a] = tmp
                queue.append([e[0],tmp])
            if e[0] == b:
                return shortest[b]
    return 0


# input
import sys
N,T = [int(num) for num in sys.stdin.readline().split()]
dp = [x[:] for x in [[-1]*(N+1)]*(N+1)]
edges = [[]]
for _ in range (N):
    edges.append([])
for _ in range (N-1):
    a,b,c = ([int(num) for num in sys.stdin.readline().split()])
    edges[a].append([b,c])
    edges[b].append([a,c])
    dp[a][b] = dp[b][a] = c

# testing distance()
'''
print "test (3,3):", distance(3,3)
print "test (5,2):", distance(5,2)
print "test (3,5):", distance(3,5)
print "test (7,3):", distance(7,3)
print "test (1,3):", distance(1,3)
print "test (5,7):", distance(5,7)
exit()
'''

# each "task" T
for _ in range (T):
    t = int(raw_input())
    nodes = [int(num) for num in sys.stdin.readline().split()]
    sum = 0
    visited_nodes = set()
    for x in nodes:
        #visited_nodes.add(x)
        for y in nodes:
            #if y not in visited_nodes:
            #    sum += distance(x,y)
            sum += distance(x,y)
    print int(sum/2)

#for i in range (1,N+1):
#    print dp[i]
