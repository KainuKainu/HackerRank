from heapq import heappush, heappop
N = int(input())
raw = [int(num) for num in input().split()]
heap = []
for item in raw:
    heappush(heap, item % (10**9 + 7))
total = 0
while heap:
    a = heappop(heap)
    b = heappop(heap)
    c = (a+b) % (10**9 + 7)
    total += c
    if heap:
        heappush(heap, c)
total = total % (10**9 + 7)
print(total)
