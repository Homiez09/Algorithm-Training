a,b,c = [int(x) for x in input().split()]
Round = max(b-a, c-b)
print(Round-1)