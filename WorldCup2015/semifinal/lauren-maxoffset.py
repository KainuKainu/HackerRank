# Swap til max offset is reduced
N = input()
array = [0] + [int(num) for num in raw_input().split()]
if all(array[i] < array[i+1] for i in range(1,N)):
    print "Cool Array"
    exit()

err = []
for i in range (1,N+1):
    err.append(i - array[i])

a = err.index(max(err))+1
b = err.index(min(err))+1
if a<b:
    print a,b
else:
    print b,a
