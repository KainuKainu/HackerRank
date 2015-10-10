N,T = [int(num) for num in input().split()]
k = int(N/2)
if k%2 == 0:
    T += k
else:
    T -= k+1
if N%2 == 1:
    k += 1
    if k%2 == 1:
        T -= k
    else:
        T += k
print(T)
