# a**2 = b**2 + c**2
import math
b, c = input().split()
B, C = float(b), float(c)
a = math.sqrt((B**2)+(C**2))
print('{:.6f}'.format(a))