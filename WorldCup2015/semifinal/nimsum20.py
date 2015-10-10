#Failteam
dp = {}
array = []
#returns all subarrays from start to end inclusive
def func(start,end):
    length = end - start
    #in dp dictionary
    if dp.has_key((start,end)):
        return dp[(start,end)]
    #only 1 element in range
    if length == 0:
        dp[(start,end)] = array[start]
        return [[array[start]]]
    #recursion
    ret = []
    tmp = func(start,end-1)
    for l in tmp:
        l.append(array[end])
        ret.append(l)
        L = len(l)-2
        if L >= 0:
            ret.append(l[:L] + [l[L]+l[L+1]])
    dp[(start,end)] = ret
    return ret

# input
N = input()
array = [int(num) for num in raw_input().split()]
subs = func(0,N-1)
ret = 0

# find XOR of each
for tmpsub in subs:
    xor = 0
    for num in tmpsub:
        xor ^= num
    if xor == 0:
        ret += 1
print ret
