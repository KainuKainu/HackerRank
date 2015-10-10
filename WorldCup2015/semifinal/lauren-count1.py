# Swap max & min until less inversions found
N = input()
array = [0] + [int(num) for num in raw_input().split()]
max_inv = 0
for i in range (1,N):
    for j in range (i+1,N+1):
        if array[j] < array[i]:
            max_inv += 1
if max_inv == 0
    print "Cool Array"
    exit()

# set error
err = [0]*N
for i in range (1,N+1):
    err[i-1]= (i - array[i])

# loop til good swap found
new_inv = max_inv
while new_inv >= max_inv:
    #swap
    a = err.index(max(err))+1
    b = err.index(min(err))+1
    array[a] += array[b]
    array[b] = array[a] - array[b]
    array[a] = array[a] - array[b]
    err[a-1] = a - array[a]
    err[b-1] = b - array[b]
    #count new inversions
    new_inv = 0
    for i in range (1,N):
        for j in range (i+1,N+1):
            if array[j] < array[i]:
                new_inv += 1

# print result
if a<b:
    print a,b
else:
    print b,a
