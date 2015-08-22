import math
l1 = float(input())
l2 = float(input())
c = u'\xb0'
a = math.degrees(math.atan(l1/l2))
a = round(a)
print(a,end="")
print(c)
