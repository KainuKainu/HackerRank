import math
import sys
l1 = float(raw_input())
l2 = float(raw_input())
a = math.degrees(math.atan(l1/l2))
a = round(a)
print "%.0f" % a,
sys.stdout.softspace=0
print u"\u00b0".encode('utf-8')
