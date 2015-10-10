from sys import stdin
N = int(stdin.readline())
weight = [0] + [int(num) for num in stdin.readline().split()]
total_sum = sum(weight)
edges = []

for edge in range(N-1):
    nodes = [int(num) for num in stdin.readline().split()]
    edges.append(nodes)

least_diff = total_sum

for i in range (N-1):
    sub_edges = edges[:]
    sub_root = sub_edges.pop(i)[0]
    tmp_sum = weight[sub_root]
    visited_edges = []
    visited_nodes = set()
    visited_nodes.add(sub_root)
    next_edges = filter(lambda edge: sub_root in edge \
            and edge not in visited_edges, sub_edges)

    #loop while queue not empty
    while next_edges:
        curr_edge = next_edges.pop()
        visited_edges.append(curr_edge)
        for x in curr_edge:
            if x not in visited_nodes:
                tmp_sum += weight[x]
                visited_nodes.add(x)
                next_edges += filter(lambda edge: x in edge \
                        and edge not in visited_edges, sub_edges)

    tmp_diff = abs(total_sum - (2*tmp_sum))
    if tmp_diff < least_diff:
        least_diff = tmp_diff

ans = int((least_diff + total_sum)/2)
print ans
