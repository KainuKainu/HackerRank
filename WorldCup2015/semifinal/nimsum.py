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

xordp = {}
def xorfunc(a,b):
    if not xordp.has_key((a,b)):
        if a == b:
            xordp[(a,b)] = 0
        elif a == 0:
            xordp[(a,b)] = b
        else:
            xordp[(a,b)] = a^b
    return xordp[(a,b)]
    '''
    if xordp.has_key((a,b)):
        return xordp[(a,b)]
    if a == b:
        xordp[(a,b)] = 0
        return 0
    if a == 0:
        xordp[(a,b)] = b
        return b
    xordp[(a,b)] = a^b
    '''

# input
N = input()
array = [int(num) for num in raw_input().split()]
subs = func(0,N-1)
ret = 0

# find XOR of each
for tmpsub in subs:
    xor = 0
    for num in tmpsub:
        #xor = xorfunc(xor,num) if xor <= num else xorfunc(num,xor)
        if xor <= num:
            xor = xorfunc(xor,num)
        else:
            xor = xorfunc(num,xor)
    if xor == 0:
        ret += 1
print ret
