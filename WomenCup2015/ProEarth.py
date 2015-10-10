N,T = [int(num) for num in input().split()]
x = -1
for a in range (1,N+1):
    T += x
    if a%2 == 0:
        if x < 0: x = -(x-1)
        else: x = -(x+1)
print(T)
