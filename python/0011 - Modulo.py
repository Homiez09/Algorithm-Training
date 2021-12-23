num = []
for i in range(10):
    num.append(int(input())%42)

count = []    
for i in num:
    x = 0
    for j in num:
        if j != i:
            x+=1
    count.append(x)
#print(num)
#print(count)
count.sort()
print(count[-1]+1)