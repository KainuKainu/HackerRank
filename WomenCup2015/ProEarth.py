N,T = [int(num) for num in input().split()]
k = int(N/6)
m = N%6
T -= k*4
if m == 1 or m == 5:
    T -= 1
elif m == 2:
    T -= 2
elif m == 4:
    T += 2
if T < 0:
    print(0)
else:
    print(T)
