# Only swap positions at max & min offsets
# Compare same offsets
N = input()
array = [0] + [int(num) for num in raw_input().split()]
if all(array[i] < array[i+1] for i in range(1,N)):
    print "Cool Array"
    exit()

err = []
for i in range (1,N+1):
    err.append(i - array[i])
#print err

#find max & min err
e_max = e_min = 0
a = 0
b = N-1
for i in range (N):
    #print "i =",i
    if err[i] <= e_min:
        if err[i] < e_min or i < a:
            a = i
            if err[i] < e_min:
                e_min = err[i]
            #print "a =",a
    elif err[i] >= e_max:
        if err[i] > e_max or i > b:
            b = i
            if err[i] > e_max:
                e_max = err[i]
            #print "b =",b
a += 1
b += 1

if a<b:
    print a,b
else:
    print b,a
