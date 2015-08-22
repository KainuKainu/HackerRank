D = {}
D["insert"] = list.insert
D["pop"] = list.pop
D["sort"] = list.sort
D["print"] = print
D["reverse"] = list.reverse
D["remove"] = list.remove
D["append"] = list.append
D["count"] = list.count
D["index"] = list.index

L = []
N = int(input())
for i in range (0,N):
    l = input().split()
    if (len(l) == 1): D[l[0]](L)
    elif (len(l) == 2): D[l[0]](L, int(l[1]))
    else: D[l[0]](L, int(l[1]), int(l[2]))
