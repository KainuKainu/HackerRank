# Python 3 solution for Maximize It
# Author: sharmaster96

#prolly what they wanna test: itertools
import itertools

k, m = [int(x) for x in input().split()]
lsts = []

for _ in range(k):
    lsts.append(sorted([(int(x)**2)%m for x in input().split()][1:]))
possibilities = itertools.product(*lsts)
maximum = max([sum(t)%m for t in possibilities])
print(maximum)
