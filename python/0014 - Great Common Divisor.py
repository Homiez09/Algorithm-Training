x, y = [int(z) for z in input().split()]
while x != 0:
    x, y = x, y%x
    x, y = y, x   
print(y)
